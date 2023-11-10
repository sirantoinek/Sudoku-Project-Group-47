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

        # save the dimensions for future reference
        self.width = width
        self.height = height

        self.selected_cell = None  # the cell the player has currently selected

    def select(self, row, col):
        """Select a cell at the given row and column"""
        '''the actual indexes are 1 less than the row and column numbers'''
        row -= 1
        col -= 1
        try:
            self.selected_cell = self.cells[col][row]
        except IndexError:
            print(f'There is no cell at ({col}, {row}). There are {self.width} columns and {self.height} rows.')

    def find_empty(self):
        """Returns tuple with row and column of an empty cell"""
        raise NotImplementedError  # FIXME: I'm not actually sure what's expected here

    def sketch(self, value):
        """Sets sketched value of selected cell"""
        self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        """Sets value of selected cell"""
        self.selected_cell.set_cell_value(value)

    def clear(self):
        """Clear the selected cell by setting both its value and sketched value back to 0"""
        if True:  # FIXME: I think this should only work for player-set values. Find a way to check
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)

    def draw(self):
        """Draw the board"""
        # FIXME: placeholder behavior
        for y in range(self.height):
            for x in range(self.width):
                print(self.cells[x][y].value, end=' ')
            print()

    def click(self, x, y):
        """Handle mouse clicks at a point on the board"""
        raise NotImplementedError("GUI not implemented")

    def is_full(self):
        """Check if the board has any empty cells left"""
        for column in self.cells:
            for cell in column:
                if cell.value == 0:  # cell is empty
                    return False
        return True  # no empty cell found

    def update_board(self):
        """Not actually sure what this function is meant to do"""
        raise NotImplementedError

    def reset_to_original(self):
        """Resets all cell values on the board (0 if cleared, otherwise the corresponding digit, whatever that means)"""
        raise NotImplementedError()

    def check_board(self):
        """Check if the board has been solved"""
        raise NotImplementedError  # FIXME: Nick will implement this function


'''Everything below this point is testing code that will only run if board.py is launched directly'''
if __name__ == "__main__":
    choices = [
        'Select',  # 1
        # 'Find empty',
        'Sketch',  # 2
        'Place number',  # 3
        'clear',  # 4
        'draw',  # 5
        # 'click',
        'Is full',  # 6
        # 'Update board',
        # 'Reset to original',
        # 'Check board'
    ]

    test_board = Board(9, 9, None, 0)
    choice = 0
    while choice != -1:
        for (index, option) in enumerate(choices):
            print(f"{index + 1}. " + option)

        choice = int(input())
        if choice == 1:
            row = int(input("Row:"))
            col = int(input("Col:"))
            test_board.select(row, col)
        elif choice == 2:
            test_board.sketch(int(input("Value:")))
        elif choice == 3:
            test_board.place_number(int(input("Value:")))
        elif choice == 4:
            test_board.clear()
        elif choice == 5:
            test_board.draw()
        elif choice == 6:
            print(test_board.is_full())
