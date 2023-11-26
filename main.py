import pygame
import main_menu
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    screen.fill(BACKGROUND_COLOR)

    game_board = None
    display_main_menu = True
    display_win = False
    display_end = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if display_main_menu:
                main_menu.displayMainMenu(screen, WIDTH, HEIGHT)
                # calls on a function that displays the main menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = main_menu.getDifficulty(event.pos)
                    # calls on a function that determines what difficulty was selected
                    if difficulty != None:
                        display_main_menu = False
                        game_board = Board(9, 9, screen, difficulty)
                        game_board.draw()
                        # if a difficulty was selected, the main menu is no longer displayed and the game is displayed

            elif game_board is not None:
                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse click
                    row, col = game_board.click(event.pos[0], event.pos[1])
                    # this decision structure below avoids crashing when the user clicks outside the board
                    if row is None or col is None:
                        pass
                    else:
                        game_board.select(row, col)

                elif event.type == pygame.KEYDOWN:
                    if pygame.key.name(event.key).isnumeric():  # if user pressed a number, sketch the value
                        value_to_sketch = int(pygame.key.name(event.key))  # get int value for the pressed number
                        game_board.sketch(value_to_sketch)

                    elif event.key == pygame.K_RETURN:  # if user pressed Enter, set the cell value
                        game_board.place_number(
                            game_board.selected_cell.sketched_value)  # set the cell's value to its sketched value...
                        game_board.sketch(0)  # ...and remove the sketched value
                        # print(game_board.check_board())  # simple test code for check_board and get_box_as_list.
                    elif game_board.selected_cell is not None:  # avoid error if player has not selected a cell yet
                        '''
                        Finally, we'll check if the player tried to move the selection using the arrow keys.
                        We start by using a dict to associate each arrow key to an offset.
                        '''
                        directions = {
                            pygame.K_UP: (0, 1),
                            pygame.K_LEFT: (-1, 0),
                            pygame.K_DOWN: (0, -1),
                            pygame.K_RIGHT: (1, 0)
                        }
                        offset = directions.get(event.key)

                        if offset is not None:
                            x_offset, y_offset = offset
                            col = game_board.selected_cell.col + x_offset
                            row = game_board.selected_cell.row - y_offset  # y values are reversed in pygame, so we subtract
                            if 0 <= col < game_board.width and 0 <= row < game_board.height:  # only allow valid selections
                                game_board.select(row, col)
                # this should call on a function that displays the game
                # potentially handles all game logic

                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = board.click(event.pos[0], event.pos[1])
                    board.select(row, col)
                    # this is the code that will be used to select a cell
                '''
    
            elif display_end:
                pass
                # this should call on a function that displays the end screen
                # would be helpful to implement as a module
                # pass it game status to correctly print if the player won or lost
                # will also include a button to take user back to the main menu

        pygame.display.update()



if __name__ == "__main__":
    main()