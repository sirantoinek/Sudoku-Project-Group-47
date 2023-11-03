"""This class is a WIP. It will be finished by Milestone 3"""
class Board:
    def __init__(self, width, height, screen, difficulty):
        """Create the board with given dimensions, window, and difficulty setting"""
        self.cells = []
        for x in range(width):
            column = []
            for y in range(height):
                column.append(0)  # FIXME: change for instances of Nick's Cell class
            self.cells.append(column)
        self.selected_row_index = 0
        self.selected_column_index = 0

    def select(self, row, col):
        """Select a cell at the given row and column"""
        self.selected_cell = self.cells[row - 1][col - 1]
        # self.selected_cell.is_selected FIXME: Nick, please include a variable in your Cell class that marks whether the instance is selected
        # FIXME: handle out of bounds values

    def find_empty(self):
        """Returns tuple with row and column of an empty cell"""
        raise NotImplementedError  # FIXME: I'm not actually sure what's expected here

    def sketch(self, value):
        """Sets sketched value of selected cell"""
        self.selected_cell = 0  # FIXME: complete with Nick's Cell class
        raise NotImplementedError

    def place_number(self, value):
        """Sets value of selected cell"""
        self.selected_cell = 0  # FIXME: complete with Nick's Cell class
        raise NotImplementedError

    def clear(self):
        """Not actually sure what this function is meant to do"""
        raise NotImplementedError

    def draw(self):
        """Draw the board"""
        raise NotImplementedError("GUI not implemented")

    def click(self, x, y):
        """Handle mouse clicks at a point on the board"""
        raise NotImplementedError("GUI not implemented")

    def is_full(self):
        """Not actually sure what this function is meant to do"""
        raise NotImplementedError

    def update_board(self):
        """Not actually sure what this function is meant to do"""
        raise NotImplementedError

    def reset_to_original(self):
        """Resets all cell values on the board (0 if cleared, otherwise the corresponding digit, whatever that means)"""
        raise NotImplementedError()

    def check_board(self):
        """Check if the board has been solved"""
        raise NotImplementedError  # FIXME: Nick will implement this function
