import locale
import os
import argparse
import curses
from importlib import resources

import sys
import subprocess
import mistune
from pathlib import Path
from . import ansi_renderer


def detect_terminal_background():
    try:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.endwin()

        if curses.can_change_color():
            r, g, b = curses.color_content(curses.COLOR_WHITE)
            if r > 500 and g > 500 and b > 500:
                return "dark"
            else:
                return "light"
    except Exception:
        pass


renderer = ansi_renderer.ANSIRenderer()
markdown = mistune.create_markdown(renderer=renderer)
dump = mistune.create_markdown(
    renderer=lambda tokens, state: ansi_renderer.dump(tokens)
)

SUPPORTED_LANGUAGES = ["en", "ja"]

parser = argparse.ArgumentParser(
    description="""noman - Man pages without the man""",
)

parser.add_argument(
    "-l",
    "--list",
    action="store_true",
    help="List all available pages",
)

parser.add_argument(
    "-L",
    "--language",
    choices=SUPPORTED_LANGUAGES,
    help="Language to use for syntax highlighting(valid: en, ja)",
)

parser.add_argument(
    "--no-pager",
    action="store_true",
    help="Do not use pager",
)


parser.add_argument(
    "-v",
    "--version",
    dest="version",
    action="store_true",
    help="Show version",
)


parser.add_argument("name", nargs="?", help="Name of the page to view")


def main():
    args = parser.parse_args()
    import noman_cli.pages.ja as ja

    if args.version:
        print("noman 0.1")
        sys.exit(0)

    lang = "en"
    if args.language:
        lang = args.language
    else:
        locale.setlocale(locale.LC_ALL, "")
        lang = locale.getlocale(locale.LC_MESSAGES)[0].split("_")[0].lower()

    if lang not in SUPPORTED_LANGUAGES:
        lang = "en"

    root = resources.files() / "pages" / lang

    if args.list:
        print("List of available pages:")
        for p in sorted(root.glob("*.md")):
            print(f"{p.stem}")
        sys.exit(0)

    if not args.name:
        print("No page name provided", file=sys.stderr)
        sys.exit(1)

    file = (root / args.name).with_suffix(".md")

    if not file.exists():
        print(f"Page {args.name} not found")
        sys.exit(1)

    src = file.read_text()

    s = markdown(src)
    if args.no_pager:
        print(s)
    else:
        p = subprocess.Popen(["less", "-R"], stdin=subprocess.PIPE)
        p.stdin.write(s.encode())
        p.stdin.close()
        sys.exit(p.wait())


if __name__ == "__main__":
    main()
