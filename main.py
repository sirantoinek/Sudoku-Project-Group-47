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

    game_board = None
    display_main_menu = True
    display_game = False
    display_end = False
    victory = NO_END

    while True:
        '''--------- Main Menu ---------'''
        background_texture = pygame.image.load("Bamboo.jpg")
        screen.blit(background_texture, (-100, 0))
        screen.blit(background_texture, (-100, 300))
        main_menu.display_main_menu(screen, WIDTH, HEIGHT)
        difficulty = None

        # calls on a function that displays the main menu
        while display_main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = main_menu.get_difficulty(event.pos)
                    # calls on a function that determines what difficulty was selected
            if difficulty != None:
                display_main_menu = False

                display_game = True
                # if a difficulty was selected, the main menu is no longer displayed and the game is displayed
            pygame.display.update()

        '''--------- Game ---------'''
        background_texture = pygame.image.load("Bamboo.jpg")
        screen.blit(background_texture, (-100, 0))
        screen.blit(background_texture, (-100, 200))
        game_board = Board(9, 9, screen, difficulty)
        game_board.draw()
        # calls on a function that displays the game
        while display_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    user_selection = game_board.click(event.pos[0], event.pos[1])
                    # saves row and column of the cell that was clicked
                    if user_selection is None:
                        pass
                    # if the user clicked outside the board, do nothing
                    elif type(user_selection) is int:
                        # use 'key' phrases to determine what button was clicked
                        if user_selection == BUTTON_RESET:
                            game_board.reset_to_original()
                            # resets the board
                        if user_selection == BUTTON_RESTART:
                            background_texture = pygame.image.load("Bamboo.jpg")
                            screen.blit(background_texture, (-100, 0))
                            screen.blit(background_texture, (-100, 200))
                            game_board = Board(9, 9, screen, difficulty)

                            game_board.draw()
                            # restarts the game with a new board but same difficulty
                        if user_selection == BUTTON_EXIT:
                            display_game = False
                            display_main_menu = True
                            # exits the game and returns to the main menu
                    else:
                        game_board.select(user_selection[0], user_selection[1])
                        # selects the cell that was clicked
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)

                    '''Numpad inputs are named '[#]', where # is the number pressed.
                    If the key's name starts and ends with brackets, we strip them away.
                    This way, the subsequent code can correctly identify numbers.'''
                    if key_name[0] == '[' and key_name[-1] == ']':
                        key_name = key_name[1:-1]

                    if key_name.isnumeric():  # if user pressed a number, sketch the value
                        value_to_sketch = int(key_name)  # get int value for the pressed number
                        game_board.sketch(value_to_sketch)

                    elif (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and game_board.selected_cell is not None:  # if user pressed Enter, set the cell value
                        game_board.place_number(game_board.selected_cell.sketched_value)  # set the cell's value to its sketched value...
                        game_board.sketch(0)  # ...and remove the sketched value
                        game_status = game_board.check_board()
                        # checks game status to see if the board is complete or won
                        if game_status == NO_END:
                            pass
                            # if the board is not complete, the game continues to be displayed
                        elif game_status == END_WIN or game_status == END_LOSE:
                            display_game = False
                            display_end = True
                            victory = True if game_status == END_WIN else False
                            # if the board is complete, the game is no longer displayed and the end screen is displayed
                            # game_status variable can be used to determine if win or loss screen should be displayed

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


            pygame.display.update()

        '''--------- End Screen ---------'''
        # here should call on a function that displays the end screen
        # would be helpful to implement as a module
        # pass it game status to correctly print if the player won or lost
        # will also include a button to take user back to the main menu
        victory_screen = GameOver(screen)
        if victory:
            victory_screen.win()
        else:
            victory_screen.loss()

        while display_end:
            # handling happens here (mouse clicks)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_board = None
                        display_main_menu = True
                        display_game = False
                        display_end = False
            pygame.display.update()





if __name__ == "__main__":
    main()
