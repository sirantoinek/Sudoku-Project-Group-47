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
    for row in range(9):
        for col in range(9):
            cell = Cell(0, row, col, screen)
            cell.set_cell_value(1)
            cell.draw_final_value()




    pygame.display.update()