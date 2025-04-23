esc = "\x1b["

codes = {}
codes[""] = ""
codes["reset"] = esc + "39;49;00m"
codes["reset-attr"] = esc + "00m"
codes["bold"] = esc + "01m"
codes["faint"] = esc + "02m"
codes["standout"] = esc + "03m"
codes["underline"] = esc + "04m"
codes["blink"] = esc + "05m"
codes["overline"] = esc + "06m"

dark_colors = ["black", "red", "green", "yellow", "blue",
               "magenta", "cyan", "gray"]
light_colors = ["brightblack", "brightred", "brightgreen", "brightyellow", "brightblue",
                "brightmagenta", "brightcyan", "white"]

x = 30
for dark, light in zip(dark_colors, light_colors):
    codes[dark] = esc + "%im" % x
    codes[light] = esc + "%im" % (60 + x)
    x += 1



print(f"{codes['red']} 赤 {codes['bold']} 赤 {codes['white']} 白 "
      f"{codes['reset-attr']} 白 {codes['reset']} 白 {codes['reset']}")



print(f"{codes['red']} 赤 {codes['blue']} 赤 {codes['white']} 白 "
      f"{codes['reset-attr']} 白 {codes['reset']} 白 {codes['reset']}")
