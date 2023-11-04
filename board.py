from cell import Cell

"""This class is a WIP. It will be finished by Milestone 3"""


# FIXME: decide whether we're using column/row numbers or indexes. Change __init__ and select accordingly
# FIXME: clear & reset_to_original functions need copy of the original board. We need to figure out where to store it
class Board:
    def __init__(self, width, height, screen, difficulty):
        """Create the board with given dimensions, window, and difficulty setting"""

        # create the board
        self.cells = []
        for x in range(width):
            column = []
            for y in range(height):
                column.append(Cell(0, x + 1, y + 1, screen))
            self.cells.append(column)

        self.selected_cell = None  # the cell the player has currently selected

    def select(self, row, col):
        """Select a cell at the given row and column"""
        self.selected_cell = self.cells[row - 1][col - 1]
        # FIXME: handle out of bounds values

    def find_empty(self):
        """Returns tuple with row and column of an empty cell"""
        raise NotImplementedError  # FIXME: I'm not actually sure what's expected here

    def sketch(self, value):
        """Sets sketched value of selected cell"""
        self.selected_cell.sketched_value = value
        raise NotImplementedError

    def place_number(self, value):
        """Sets value of selected cell"""
        self.selected_cell.value = value
        raise NotImplementedError

    def clear(self):
        """Clear the selected cell"""
        if True:  # FIXME: I think this should only work for player-selected values. Find a way to check
            self.selected_cell.value = 0
            self.selected_cell.sketched_value = 0

    def draw(self):
        """Draw the board"""
        raise NotImplementedError("GUI not implemented")

    def click(self, x, y):
        """Handle mouse clicks at a point on the board"""
        raise NotImplementedError("GUI not implemented")

    def is_full(self):
        """Check if the board has any empty cells left"""
        for column in self.cells:
            for cell in column:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        """Not actually sure what this function is meant to do"""
        raise NotImplementedError

    def reset_to_original(self):
        """Resets all cell values on the board (0 if cleared, otherwise the corresponding digit, whatever that means)"""
        raise NotImplementedError()

    def check_board(self):
        """Check if the board has been solved"""
        raise NotImplementedError  # FIXME: Nick will implement this function
