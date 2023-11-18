import pygame
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell
from constants import *

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
            pass
            # this should call on a function that displays the main menu
            # the function should return a game difficulty and should update display_game to True
            # feel free to change this logic if it doesn't work right
        if display_game:
            pass
            # this should call on a function that displays the game





    pygame.display.update()