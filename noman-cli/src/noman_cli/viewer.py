import locale
import argparse
import curses
from importlib import resources
from collections import defaultdict
import sys
import subprocess
import mistune
import random
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


def levenshtein_distance(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)

    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[len_s1][len_s2]


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
    help="Language to display noman page (valid: en, ja)",
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
        candidates = defaultdict(list)
        for name in [n.stem for n in root.iterdir()]:
            d = levenshtein_distance(name, args.name)
            candidates[d].append(name)

        candidates = sorted(candidates.items())[0][1]
        if len(candidates) > 3:
            candidates = random.choices(candidates, k=3)
        print(
            f"Page {args.name} not found. Did you mean {' '.join(c + '?' for c in candidates)}"
        )
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
