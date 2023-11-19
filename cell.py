import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.cell_font = pygame.font.Font(None, VALUE_FONT_SIZE)
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
    
    def draw_sketched_value(self): # pass this function sketched value
        if self.sketched_value == 0:
            cell_num_surface = self.cell_font.render(None, 0, SELECTED_CELL_COLOR)
        else:
            cell_num_surface = self.cell_font.render(str(self.sketched_value), 0, SELECTED_CELL_COLOR)
        cell_num_rect = cell_num_surface.get_rect(center=(CELL_SIZE * self.col + CELL_SIZE / 2 + 22.5, CELL_SIZE * self.row + CELL_SIZE / 2  + 22.5))
        self.screen.blit(cell_num_surface, cell_num_rect)

    def draw_final_value(self):  # when user hits enter, this function should be called
        if self.value == 0:
            cell_num_surface = self.cell_font.render(None, 0, FONT_COLOR)
        else:
            cell_num_surface = self.cell_font.render(str(self.value), 0, FONT_COLOR)
        cell_num_rect = cell_num_surface.get_rect(center=(CELL_SIZE * self.col + CELL_SIZE / 2 + 22.5, CELL_SIZE * self.row + CELL_SIZE / 2 + 22.5))
        self.screen.blit(cell_num_surface, cell_num_rect)

        # method draws cell on the screen
        # this is where pygame is needed