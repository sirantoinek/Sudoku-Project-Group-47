import sys

import pygame

from cell import Cell
import sudoku_generator
import random

from constants import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        """Create the board with given dimensions, window, and difficulty setting"""

        '''Creates the 2d lists that will store cell info
        original_cells contains the raw ints generated by sudoku_generator
        cells contains the actual Cell instances derived from the ints in original_cells'''
        empty_cells = 30 + 10 * difficulty
        self.original_cells = sudoku_generator.generate_sudoku(9, empty_cells)
        self.cells = []
        for x in range(width):
            column = []
            for y in range(height):
                column.append(Cell(self.original_cells[x][y], y, x, screen))
            self.cells.append(column)

        # save the dimensions for future reference
        self.width = width
        self.height = height

        self.screen = screen

        self.selected_cell = None  # the cell the player has currently selected

    def select(self, row, col):
        """Select a cell at the given row and column"""
        try:
            self.selected_cell = self.cells[col][row]
            self.draw()  # update the display
        except IndexError:
            print(f'There is no cell at ({col}, {row}). There are {self.width} columns and {self.height} rows.')

    def find_empty(self):
        """Returns tuple with row and column of an empty cell"""
        if self.is_full():
            return None

        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.cells[x][y].value == 0:
                return x, y

    def sketch(self, value):
        """Sets sketched value of selected cell"""
        if self.original_cells[self.selected_cell.col][self.selected_cell.row] == 0:
            self.selected_cell.set_sketched_value(value)
            self.draw()  # update the display

    def place_number(self, value):
        """Sets value of selected cell"""
        if self.original_cells[self.selected_cell.col][self.selected_cell.row] == 0:
            self.selected_cell.set_cell_value(value)
            self.draw()  # update the display

    def clear(self):
        """Clears the selected cell by setting both its value and sketched value back to 0"""
        if self.original_cells[self.selected_cell.row][self.selected_cell.col] != 0:  # this cell was generated by default and can not be changed
            return

        self.selected_cell.set_cell_value(0)
        self.selected_cell.set_sketched_value(0)

        self.draw()  # update the display

    def draw(self):
        """Draws the board"""

        '''Draw the background'''
        w = pygame.image.load("Bamboo.jpg")
        self.screen.blit(w, (-100, 0))
        self.screen.blit(w, (-100, 200))

        '''Draw the grid'''
        '''Create variables specifying the area covered by this board'''
        start_x, end_x = LEFT_MARGIN, self.screen.get_width() - RIGHT_MARGIN
        start_y, end_y = TOP_MARGIN, self.screen.get_height() - BOTTOM_MARGIN
        range_x, range_y = end_x - start_x, end_y - start_y

        '''List of the x and y coordinates that will have lines through them'''
        lines_x = [(i / 9) * range_x + start_x for i in range(0, 10)]
        lines_y = [(i / 9) * range_y + start_y for i in range(0, 10)]
        wide_lines_x, wide_lines_y = lines_x[::3], lines_y[::3]  # these coordinates will have wider lines

        # draw horizontal lines
        for y in lines_y:
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (start_x, y),
                (end_x, y),
                10 if y in wide_lines_y else 5
            )

        # draw vertical lines
        for x in lines_x:
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (x, start_y),
                (x, end_y),
                10 if x in wide_lines_x else 5
            )

        # draw outline for selected cell
        if self.selected_cell is not None:
            '''Drawing the selected cell will involve drawing 4 red lines
            For convenience, let's store the relevant coordinates'''
            low_x, high_x = lines_x[self.selected_cell.col], lines_x[self.selected_cell.col + 1]
            low_y, high_y = lines_y[self.selected_cell.row], lines_y[self.selected_cell.row + 1]

            '''This list of tuples will store the start and end points of each of the 4 lines'''
            lines = [
                ((low_x, low_y), (high_x, low_y)),  # up
                ((low_x, low_y), (low_x, high_y)),  # left
                ((low_x, high_y), (high_x, high_y)),  # down
                ((high_x, low_y), (high_x, high_y)),  # right
            ]

            '''Loop through all the lines to draw them'''
            for line in lines:
                start, end = line  # unpack the line tuple to get its start and end coordinates
                pygame.draw.line(
                    self.screen,
                    SELECTION_COLOR,
                    start,
                    end,
                    5
                )

        # draw cells
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y].draw()

        self.draw_quick_menu()  # calls on a function that displays the quick menu at the bottom of the screen

        pygame.display.update()

    def draw_quick_menu(self):
        """Draws the three options under the grid"""
        menu_options = ["Reset", "Restart", "Exit"]
        menu_options_font = pygame.font.Font(None, BUTTON_FONT_SIZE)

        pygame.draw.rect(self.screen, BUTTON_COLOR, (190, 825, 110, 50))
        # this rectangle creates a fill with the secondary color
        pygame.draw.rect(self.screen, DEFAULT_FONT_COLOR, (190, 825, 110, 50), 3)
        # this rectangle creates an outline with a width of 3 pixels
        reset_menu_options_surface = menu_options_font.render(menu_options[0], 0, BUTTON_FONT_COLOR)
        reset_menu_options_rect = reset_menu_options_surface.get_rect(center=(WIDTH / 2 - 207, HEIGHT - 50))
        self.screen.blit(reset_menu_options_surface, reset_menu_options_rect)
        # the font is rendered and placed on the screen above the rectangles to create a button
        
        pygame.draw.rect(self.screen, BUTTON_COLOR, (375, 825, 150, 50))
        # this rectangle creates a fill with the secondary color
        pygame.draw.rect(self.screen, DEFAULT_FONT_COLOR, (375, 825, 150, 50), 3)
        # this rectangle creates an outline with a width of 3 pixels
        restart_menu_options_surface = menu_options_font.render(menu_options[1], 0, BUTTON_FONT_COLOR)
        restart_menu_options_rect = restart_menu_options_surface.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        self.screen.blit(restart_menu_options_surface, restart_menu_options_rect)
        # the font is rendered and placed on the screen above the rectangles to create a button

        pygame.draw.rect(self.screen, BUTTON_COLOR, (600, 825, 100, 50))
        # this rectangle creates a fill with the secondary color
        pygame.draw.rect(self.screen, DEFAULT_FONT_COLOR, (600, 825, 100, 50), 3)
        # this rectangle creates an outline with a width of 3 pixels
        exit_menu_options_surface = menu_options_font.render(menu_options[2], 0, BUTTON_FONT_COLOR)
        exit_menu_options_rect = exit_menu_options_surface.get_rect(center=(WIDTH / 2 + 200, HEIGHT - 50))
        self.screen.blit(exit_menu_options_surface, exit_menu_options_rect)
        # the font is rendered and placed on the screen above the rectangles to create a button

    def click(self, x, y):
        """Identifies which game element was clicked on"""

        if 200 < x < 300 and 825 < y < 875:
            return RESET
        elif 375 < x < 525 and 825 < y < 875:
            return RESTART
        elif 600 < x < 700 and 825 < y < 875:
            return EXIT
        # uses ranges to determine if a user clicked on a button
        # uses special 'key' phrases to determine which button was clicked
        elif x < LEFT_MARGIN or x > self.screen.get_width() - RIGHT_MARGIN or y < TOP_MARGIN or y > self.screen.get_height() - BOTTOM_MARGIN:
            return None
        # returns None if nothing of significance was clicked
        else:
            return (int((y - TOP_MARGIN) // CELL_SIZE), int((x - LEFT_MARGIN) // CELL_SIZE))
        # returns the row and column of the clicked cell

    def is_full(self):
        """Checks if the board has any empty cells left"""
        for column in self.cells:
            for cell in column:
                if cell.value == 0:  # cell is empty
                    return False
        return True  # no empty cell found

    def reset_to_original(self):
        """Resets all cell values on the board to their originally generated values"""
        for x in range(self.width):
            for y in range(self.height):
                current_cell = self.cells[x][y]
                current_cell.set_cell_value(self.original_cells[x][y])
                current_cell.set_sketched_value(0)

        self.draw()  # update the display

    def check_board(self):
        """Checks if the board has been solved
        Returns NO_END if game is unfinished, END_WIN if player won the game, or END_LOSE if player lost the game"""
        valid_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        victory = END_WIN
        for row in range(self.height):  # Checking all rows
            temp_set = []
            for col in range(self.width):
                temp_set.append((self.cells[row][col]).get_cell_value())
                # Appending cell values from the row to a temporary list to be checked.
            temp_set.sort()
            if 0 in temp_set:  # If board is incomplete, return 0.
                return NO_END
            elif temp_set != valid_set:
                victory = END_LOSE  # If the sorted row is not equal to the given valid list, the solution is incorrect.

        for col in range(self.width):  # Checking all columns
            temp_set = []
            for row in range(self.height):
                temp_set.append((self.cells[row][col]).get_cell_value())
                # Appending cell values from the column to a temporary list to be checked.
            temp_set.sort()
            if 0 in temp_set:  # If board is incomplete, return 0.
                return NO_END
            elif temp_set != valid_set:
                victory = END_LOSE  # If the sorted column is not equal to the given valid list, the solution is incorrect.

        for row in range(0, self.height, 3):  # Checking all boxes
            for col in range(0, self.width, 3):
                temp_set = self.get_box_as_list(row, col)
                temp_set.sort()
                if 0 in temp_set:  # If board is incomplete, return 0.
                    return NO_END
                elif temp_set != valid_set:
                    victory = END_LOSE  # If the sorted box is not equal to the given valid list, the solution is incorrect.

        return victory  # 1 is returned if the board was solved correctly, 2 is returned if incorrect.

    def get_box_as_list(self, row_start, col_start):
        """Returns the box starting at the given row and column as a one dimensional list."""
        box_as_list = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                box_as_list.append((self.cells[row][col]).get_cell_value())
        return box_as_list
