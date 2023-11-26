import pygame
from constants import *


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.value_font = pygame.font.Font(None, VALUE_FONT_SIZE)
        self.sketched_font = pygame.font.Font(None, SKETCHED_FONT_SIZE)
        # initialise variables

    def set_cell_value(self, value):  # pass this function sketched value
        self.value = value
        #return self.value
        # method that sets the value of the cell
        # should be called when user hits enter
        # returns the value of the cell (although this is may not be needed)

    def get_cell_value(self):  # getter for value
        return self.value

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

    def draw_sketched_value(self):  # pass this function sketched value
        if self.sketched_value != 0:
            start_x, end_x = LEFT_MARGIN, self.screen.get_width() - RIGHT_MARGIN
            start_y, end_y = TOP_MARGIN, self.screen.get_height() - BOTTOM_MARGIN
            range_x, range_y = end_x - start_x, end_y - start_y

            x = (range_x / 9) * (self.col + 0.2) + start_x
            y = (range_y / 9) * (self.row + 0.3) + start_y

            cell_num_surface = self.sketched_font.render(str(self.sketched_value), 0, SECONDARY_FONT_COLOR)
            cell_num_rect = cell_num_surface.get_rect(center=(x, y))
            self.screen.blit(cell_num_surface, cell_num_rect)

    def draw_final_value(self):  # when user hits enter, this function should be called
        if self.value != 0:
            start_x, end_x = LEFT_MARGIN, self.screen.get_width() - RIGHT_MARGIN
            start_y, end_y = TOP_MARGIN, self.screen.get_height() - BOTTOM_MARGIN
            range_x, range_y = end_x - start_x, end_y - start_y

            x = (range_x / 9) * (self.col + 0.5) + start_x
            y = (range_y / 9) * (self.row + 0.5) + start_y

            cell_num_surface = self.value_font.render(str(self.value), 0, DEFAULT_FONT_COLOR)
            cell_num_rect = cell_num_surface.get_rect(center=(x, y))
            self.screen.blit(cell_num_surface, cell_num_rect)

        # method draws cell on the screen
        # this is where pygame is needed

    def draw(self):
        self.draw_sketched_value()
        self.draw_final_value()
