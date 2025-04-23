import curses

def detect_terminal_background():
    try:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.endwin()
        
        # -1が透明色（端末のデフォルト色）を表す
        # 端末のデフォルト色がどのように表示されるか確認
        if curses.can_change_color():
            r, g, b = curses.color_content(curses.COLOR_WHITE)
            print(r, g, b)
            # 白が明るく表示される場合は暗い背景
            if r > 500 and g > 500 and b > 500:
                return "dark"
            else:
                return "light"
    except:
        pass

print(detect_terminal_background())
