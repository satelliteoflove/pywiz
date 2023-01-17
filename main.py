import curses
import textwrap


def main(stdscr):
    # Set up color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Get the terminal size
    height, width = stdscr.getmaxyx()

    # Create the three boxes
    info_box = curses.newwin(height // 2 - 2, width // 2 - 2, 1, 1)
    map_box = curses.newwin(height // 2 - 2, width // 2 - 2, 1, width // 2 + 1)
    text_box = curses.newwin(height // 2 - 2, width - 2, height // 2 + 1, 1)

    long_string = "This is a long enough string that it should reach the end \
        of the box, and hopefully return.  The idea here is that I can test \
        word wrapping and I really hope the test goes well."
    wrapped_string = textwrap.wrap(long_string, width // 2 - 2)

    # Set the text for the boxes
    for i, line in enumerate(wrapped_string):
        info_box.addstr(i + 1, 2, line, curses.color_pair(1))
    map_box.addstr(1, 2, long_string, curses.color_pair(1))
    text_box.addstr(1, 2, long_string, curses.color_pair(1))

    # Draw borders around the boxes
    info_box.box()
    map_box.box()
    text_box.box()

    # Refresh the screen to display the boxes
    stdscr.refresh()
    info_box.refresh()
    map_box.refresh()
    text_box.refresh()

    # Wait for the user to press a key
    stdscr.getch()


curses.wrapper(main)
