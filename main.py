import pygame
import sys
import main_menu
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell
from constants import *
from game_over import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    background_texture = pygame.image.load("Bamboo.jpg")

    game_board = None  # the sudoku board
    current_screen = SCREEN_MENU  # the game screen the player is currently seeing
    victory = None  # whether the game ended in a win or loss
    needs_drawing = True  # indicates whether the screen needs to be redrawn at the end of this game loop

    while True:
        '''Handle the events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # every screen has the same quit behavior
                pygame.quit()
                sys.exit()
            else:
                '''Events other than QUIT are handled differently by each screen'''
                if current_screen == SCREEN_MENU:
                    '''--------- Main Menu ---------'''
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        difficulty = main_menu.get_difficulty(event.pos)  # get the selected difficulty
                        if difficulty is not None:  # player may have clicked outside the difficulty buttons
                            current_screen = SCREEN_GAME
                            game_board = Board(9, 9, screen, difficulty)
                            needs_drawing = True  # we need to redraw and put the board on the screen

                elif current_screen == SCREEN_GAME:
                    '''--------- Game ---------'''
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        user_selection = game_board.click(event.pos[0], event.pos[1])  # the screen element that was clicked
                        if user_selection is not None:
                            if type(user_selection) is int:  # the user clicked on one of the buttons
                                if user_selection == BUTTON_RESET:
                                    game_board.reset_to_original()
                                    # resets the board to initial state
                                if user_selection == BUTTON_RESTART:
                                    current_screen = SCREEN_MENU
                                    # returns player to the main menu
                                if user_selection == BUTTON_EXIT:
                                    pygame.quit()
                                    sys.exit()
                                    # ends the program
                            else:  # the user clicked a cell on the board itself
                                game_board.select(user_selection[0], user_selection[1])
                                # selects the cell that was clicked

                            needs_drawing = True  # anything the user clicked on will cause visual changes

                    elif event.type == pygame.KEYDOWN:
                        if game_board.selected_cell is not None:  # all key input behaviors require a cell to be selected
                            key_name = pygame.key.name(event.key)

                            '''Numpad inputs are named '[#]', where # is the number pressed.
                            If the key's name starts and ends with brackets, we strip them away.
                            This way, the subsequent code can correctly identify numbers.'''
                            if key_name[0] == '[' and key_name[-1] == ']':
                                key_name = key_name[1:-1]

                            if key_name.isnumeric():  # if user pressed a number, sketch the value
                                value_to_sketch = int(key_name)  # get int value for the pressed number
                                game_board.sketch(value_to_sketch)
                                needs_drawing = True

                            else:
                                '''Check if the player entered the sketched value using Enter.
                                We'll check for both Enter keys: the main one and the one on the numpad.'''
                                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                                    game_board.place_number(game_board.selected_cell.sketched_value)  # set the cell's value to its sketched value...
                                    game_board.sketch(0)  # ...and remove the sketched value
                                    game_status = game_board.check_board()  # checks game status to see if the player won or lost
                                    if game_status == END_WIN or game_status == END_LOSE:
                                        current_screen = SCREEN_END
                                        victory = True if game_status == END_WIN else False
                                    needs_drawing = True  # we changed a value and maybe even finished the game; definitely redraw

                                '''Finally, we'll check if the player tried to move the selection using the arrow keys.
                                We start by using a dict to associate each arrow key to an offset.'''
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
                                        needs_drawing = True

                elif current_screen == SCREEN_END:
                    '''--------- End Screen ---------'''
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_board = None
                            current_screen = SCREEN_MENU
                            needs_drawing = True

        '''If any of the events could've caused visual changes, we'll redraw the screen'''
        if needs_drawing:
            '''All screens have the same background'''
            screen.blit(background_texture, (-100, 0))
            screen.blit(background_texture, (-100, 300))

            '''We call the appropriate functions for the current screen'''
            if current_screen == SCREEN_MENU:
                main_menu.display_main_menu(screen, WIDTH, HEIGHT)
            elif current_screen == SCREEN_GAME:
                game_board.draw()
            elif current_screen == SCREEN_END:
                victory_screen = GameOver(screen)
                if victory:
                    victory_screen.win()
                else:
                    victory_screen.loss()
            pygame.display.update()
            needs_drawing = False  # we won't draw again until there are more changes




if __name__ == "__main__":
    main()
