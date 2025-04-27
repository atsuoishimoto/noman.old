import locale
import os
import argparse

import sys
import subprocess
import mistune
from pathlib import Path
from . import ansi_renderer


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


parser.add_argument("name", nargs=1, help="Name of the page to view")


def main():
    args = parser.parse_args()

    if args.version:
        print("noman 0.1")
        sys.exit(0)

    if args.list:
        print("List of available pages:")
        for p in Path(".").glob("*.md"):
            print(f" - {p.stem}")
        sys.exit(0)

    lang = "en"
    if args.language:
        lang = args.language
    else:
        locale.setlocale(locale.LC_ALL, "")
        lang = locale.getlocale(locale.LC_MESSAGES)[0].split("_")[0].lower()

    if lang not in SUPPORTED_LANGUAGES:
        lang = "en"

    filename = Path(args.name[0])
    print(filename)
    src = filename.read_text()

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
