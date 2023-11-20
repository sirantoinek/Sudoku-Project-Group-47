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

    display_main_menu = True
    display_game = False
    display_win = False

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
                        display_game = True
                        # if a difficulty was selected, the main menu is no longer displayed and the game is displayed
            if display_game:
                pass
                # this should call on a function that displays the game
                # potentially handles all game logic
            if display_end:
                pass
                # this should call on a function that displays the end screen
                # would be helpful to implement as a module
                # pass it game status to correctly print if the player won or lost
                # will also include a button to take user back to the main menu
        pygame.display.update()


if __name__ == "__main__":
    main()