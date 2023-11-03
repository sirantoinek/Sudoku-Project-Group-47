import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        # initialise variables

    def set_cell_value(self, value):
        self.value = value
        # sets the value of the cell
        set_sketched_value(value)
        # uses current value as argument for sketch method

    def set_sketched_value(self, value,):
        if value != 0:
            self.sketched_value = value
        # the cell draws value if value is not 0
        else: 
            self.sketched_value = None
        # the cell should be empty if value is 0
        # uses None as a placeholder for empty cell
        

    def draw(self):
        pass
        # method draws cell on the screen
        # this is where pygame is needed