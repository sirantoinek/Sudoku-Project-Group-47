import pygame
from constants import *

def displayMainMenu(screen, width, height):
    screen.fill(BACKGROUND_COLOR)

    displayTitle(screen, width, height)
    displaySubTitle(screen, width, height)
    displayDifficulty(screen, width, height)

def getDifficulty(mouse_pos):
    if mouse_pos[0] >= 200 and mouse_pos[0] <= 300 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return "Easy"
    elif mouse_pos[0] >= 375 and mouse_pos[0] <= 525 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return "Medium"
    elif mouse_pos[0] >= 600 and mouse_pos[0] <= 700 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return "Hard"
    else:
        return None
    

'''
----------------------------------------------------------------
The following functions are helper functions for displayMainMenu
----------------------------------------------------------------
'''

def displayTitle(screen, width, height):
    title_screen_font = pygame.font.Font(None, 100)
    title_surface = title_screen_font.render("Welcome to Sudoku", 0, FONT_COLOR)
    title_rect = title_surface.get_rect(center=(width / 2, 200))
    screen.blit(title_surface, title_rect)

def displaySubTitle(screen, width, height):
    game_mode_font = pygame.font.Font(None, 75)
    game_mode_surface = game_mode_font.render("Choose a game mode!", 0, FONT_COLOR,)
    game_mode_rect = game_mode_surface.get_rect(center=(width / 2, 425))
    screen.blit(game_mode_surface, game_mode_rect)

def displayDifficulty(screen, width, height):
    game_modes = ["Easy", "Medium", "Hard"]
    game_modes_font = pygame.font.Font(None, 50)

    
    pygame.draw.rect(screen, SECONDARY_COLOR, (200, 525, 100, 50))
    pygame.draw.rect(screen, FONT_COLOR, (200, 525, 100, 50), 3)
    easy_game_modes_surface = game_modes_font.render(game_modes[0], 0, SECONDARY_FONT_COLOR,)
    easy_game_modes_rect = easy_game_modes_surface.get_rect(center=(width / 2 - 200, height / 2 + 100))
    screen.blit(easy_game_modes_surface, easy_game_modes_rect)

    pygame.draw.rect(screen, SECONDARY_COLOR, (375, 525, 150, 50))
    pygame.draw.rect(screen, FONT_COLOR, (375, 525, 150, 50), 3)
    medium_game_modes_surface = game_modes_font.render(game_modes[1], 0, SECONDARY_FONT_COLOR,)
    medium_game_modes_rect = medium_game_modes_surface.get_rect(center=(width / 2, height / 2 + 100))
    screen.blit(medium_game_modes_surface, medium_game_modes_rect)

    pygame.draw.rect(screen, SECONDARY_COLOR, (600, 525, 100, 50))
    pygame.draw.rect(screen, FONT_COLOR, (600, 525, 100, 50), 3)
    hard_game_modes_surface = game_modes_font.render(game_modes[2], 0, SECONDARY_FONT_COLOR,)
    hard_game_modes_rect = hard_game_modes_surface.get_rect(center=(width / 2 + 200, height / 2 + 100))
    screen.blit(hard_game_modes_surface, hard_game_modes_rect)


