from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.addstr("Hello")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)