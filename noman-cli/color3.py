from enum import StrEnum


class fg(StrEnum):
    reset = "\033[39m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    default = "\033[39m"
    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"


class bg(StrEnum):
    reset = "\033[49m"
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    white = "\033[47m"
    default = "\033[49m"
    bright_black = "\033[100m"
    bright_red = "\033[101m"
    bright_green = "\033[102m"
    bright_yellow = "\033[103m"
    bright_blue = "\033[104m"
    bright_magenta = "\033[105m"
    bright_cyan = "\033[106m"
    bright_white = "\033[107m"


class attr(StrEnum):
    reset = "\033[0m"
    bold = "\033[1m"
    faint = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    blink = "\033[5m"
    reverse = "\033[7m"
    conceal = "\033[8m"
    strike = "\033[9m"


print("デフォルト", fg.red, "赤", fg.reset, bg.green, "デフォルト", attr.reset)
