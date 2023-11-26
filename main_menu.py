import pygame
from constants import *

def displayMainMenu(screen, width, height):
    screen.fill(BACKGROUND_COLOR)
# fills screen with background color
    displayTitle(screen, width, height)
    displaySubTitle(screen, width, height)
    displayDifficulty(screen, width, height)
# calls all functions to display screen elements

def getDifficulty(mouse_pos):
    if mouse_pos[0] >= 200 and mouse_pos[0] <= 300 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return DIFFICULTY_EASY
    elif mouse_pos[0] >= 375 and mouse_pos[0] <= 525 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return DIFFICULTY_MEDIUM
    elif mouse_pos[0] >= 600 and mouse_pos[0] <= 700 and mouse_pos[1] >= 525 and mouse_pos[1] <= 575:
        return DIFFICULTY_HARD
    else:
        return None
# receives mouse click coordinates and determines what difficulty was selected using ranges
# if the click was 'out of bounds', returns None

'''
----------------------------------------------------------------
The following functions are helper functions for displayMainMenu
----------------------------------------------------------------
'''

def displayTitle(screen, width, height):
    title_screen_font = pygame.font.Font(None, 100)
    title_surface = title_screen_font.render("Welcome to Sudoku", 0, DEFAULT_FONT_COLOR)
    title_rect = title_surface.get_rect(center=(width / 2, 200))
    screen.blit(title_surface, title_rect)
# displays title of game

def displaySubTitle(screen, width, height):
    game_mode_font = pygame.font.Font(None, 75)
    game_mode_surface = game_mode_font.render("Choose a game mode!", 0, DEFAULT_FONT_COLOR)
    game_mode_rect = game_mode_surface.get_rect(center=(width / 2, 425))
    screen.blit(game_mode_surface, game_mode_rect)
# displays subtitle of game

def displayDifficulty(screen, width, height):
    game_modes = ["Easy", "Medium", "Hard"]
    game_modes_font = pygame.font.Font(None, 50)
    # creates a list of game modes and a font for the game modes

    pygame.draw.rect(screen, SECONDARY_COLOR, (200, 525, 100, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, DEFAULT_FONT_COLOR, (200, 525, 100, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    easy_game_modes_surface = game_modes_font.render(game_modes[0], 0, BUTTON_FONT_COLOR)
    easy_game_modes_rect = easy_game_modes_surface.get_rect(center=(width / 2 - 200, height / 2 + 100))
    screen.blit(easy_game_modes_surface, easy_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button

    pygame.draw.rect(screen, SECONDARY_COLOR, (375, 525, 150, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, DEFAULT_FONT_COLOR, (375, 525, 150, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    medium_game_modes_surface = game_modes_font.render(game_modes[1], 0, BUTTON_FONT_COLOR)
    medium_game_modes_rect = medium_game_modes_surface.get_rect(center=(width / 2, height / 2 + 100))
    screen.blit(medium_game_modes_surface, medium_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button

    pygame.draw.rect(screen, SECONDARY_COLOR, (600, 525, 100, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, DEFAULT_FONT_COLOR, (600, 525, 100, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    hard_game_modes_surface = game_modes_font.render(game_modes[2], 0, BUTTON_FONT_COLOR)
    hard_game_modes_rect = hard_game_modes_surface.get_rect(center=(width / 2 + 200, height / 2 + 100))
    screen.blit(hard_game_modes_surface, hard_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button