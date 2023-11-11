import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        # initialise variables

    def set_cell_value(self, value): # pass this function sketched value
        self.value = value
        return self.value
        # method that sets the value of the cell
        # should be called when user hits enter
        # returns the value of the cell (although this is may not be needed)

    def set_sketched_value(self, value):
        try:
            if value >= 1 and value <= 9:
                self.sketched_value = value
            else: 
                raise ValueError
        except ValueError:
            self.sketched_value = 0
        finally:
            return self.sketched_value
        
        # method that sets the sketched value of the cell
        # should be called when user hits a number
        # sets the sketched value to 0 if the user input is invalid in any way
        # 0 is placeholder for no sketched value
    

    def draw(self):
        pass
        # method draws cell on the screen
        # this is where pygame is needed