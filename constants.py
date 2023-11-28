# THIS IS A FILE OF CONSTANTS, MEANT TO CREATE STANDARDS FOR UI ELEMENTS

GRID_COLOR = (24, 29, 39)  # the color used to draw the sudoku gridlines
SELECTION_COLOR = (240, 29, 39)  # the color used to highlight the player-selected cell

DEFAULT_FONT_COLOR = (24, 29, 39)  # the color for most text, including menus and cell values
SKETCHED_FONT_COLOR = (110, 110, 110)  # the color used for sketched cell values
BUTTON_FONT_COLOR = (240, 244, 239)  # the color used for the text on menu buttons

BUTTON_COLOR = (1, 111, 185)  # the color used for menu buttons

WIDTH = 900  # width of the game window
HEIGHT = 900  # height of the game window
TOP_MARGIN = 10  # empty space between the grid and top of game window
BOTTOM_MARGIN = 100  # space between the grid and bottom of game window (not empty as the quick menu goes here)
LEFT_MARGIN = 55  # empty space between the grid and left of game window
RIGHT_MARGIN = 55  # empty space between the grid and right of game window

CELL_SIZE = (WIDTH - (TOP_MARGIN + BOTTOM_MARGIN)) / 9  # the width of an individual cell

TITLE_FONT_SIZE = 100  # font size for menu titles
BUTTON_FONT_SIZE = 50  # font size for text in buttons
VALUE_FONT_SIZE = 70  # cell value font size
SKETCHED_FONT_SIZE = 60  # sketched cell value font size

DIFFICULTY_EASY = 0  # easy mode ID
DIFFICULTY_MEDIUM = 1  # medium mode ID
DIFFICULTY_HARD = 2  # hard mode ID

BUTTON_RESET = 0  # quick menu reset ID
BUTTON_RESTART = 1  # quick menu restart ID
BUTTON_EXIT = 2  # quick menu exit ID

NO_END = 0  # indicates game is ongoing
END_WIN = 1  # indicates game ended in a victory for the player
END_LOSE = 2  # indicates game ended in a loss for the player

