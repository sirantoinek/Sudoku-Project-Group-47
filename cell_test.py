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
            x = Board(9,9,screen,"easy")
            y = x.give_cells()
            cell.set_cell_value(y[row][col])
            cell.draw_final_value()
    z = 0
    for i in range(9):
        print(y[i])
        z += 1
        if i == 8:
            break
        if z == 3:
            print("-----------------------")
            z = 0
    pygame.draw.line(screen, GRID_COLOR, (25, 0), (25, 900), 10)
    for i in range(1,10):
        if i % 3 == 0:
            pygame.draw.line(screen, GRID_COLOR, (i * CELL_SIZE + 25, 0), (i * CELL_SIZE + 25, 900), 10)
            pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE + 25), (900, i * CELL_SIZE + 25), 10)
            continue
        pygame.draw.line(screen,GRID_COLOR,(i * CELL_SIZE + 25, 0), (i * CELL_SIZE + 25, 900), 3)
        pygame.draw.line(screen, GRID_COLOR, (0, i * CELL_SIZE + 25), (900, i * CELL_SIZE + 25), 3)
    pygame.display.update()
    pygame.time.wait(15000)