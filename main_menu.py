import pygame
from constants import *
import glob


def display_main_menu(screen, width, height):
    display_title(screen, width, height)
    display_subtitle(screen, width, height)
    display_difficulty(screen, width, height)
# calls all functions to display screen elements


def get_difficulty(mouse_pos):
    if 200 <= mouse_pos[0] <= 300 and 525 <= mouse_pos[1] <= 575:
        return DIFFICULTY_EASY
    elif 375 <= mouse_pos[0] <= 525 <= mouse_pos[1] <= 575:
        return DIFFICULTY_MEDIUM
    elif 600 <= mouse_pos[0] <= 700 and 525 <= mouse_pos[1] <= 575:
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


def display_title(screen, width, height):
    title_screen_font = pygame.font.Font(None, TITLE_FONT_SIZE)
    title_surface = title_screen_font.render("Welcome to Sudoku", 0, DEFAULT_FONT_COLOR)
    title_rect = title_surface.get_rect(center=(width / 2, 200))
    screen.blit(title_surface, title_rect)
# displays title of game


def display_subtitle(screen, width, height):
    game_mode_font = pygame.font.Font(None, 75)
    game_mode_surface = game_mode_font.render("Choose a game mode!", 0, DEFAULT_FONT_COLOR)
    game_mode_rect = game_mode_surface.get_rect(center=(width / 2, 425))
    screen.blit(game_mode_surface, game_mode_rect)
# displays subtitle of game


def display_difficulty(screen, width, height):
    game_modes = ["Easy", "Medium", "Hard"]
    game_modes_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
    # creates a list of game modes and a font for the game modes

    pygame.draw.rect(screen, BUTTON_COLOR, (200, 525, 100, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, BUTTON_OUTLINE_COLOR, (200, 525, 100, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    easy_game_modes_surface = game_modes_font.render(game_modes[0], 0, BUTTON_FONT_COLOR)
    easy_game_modes_rect = easy_game_modes_surface.get_rect(center=(width / 2 - 200, height / 2 + 100))
    screen.blit(easy_game_modes_surface, easy_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button

    pygame.draw.rect(screen, BUTTON_COLOR, (375, 525, 150, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, BUTTON_OUTLINE_COLOR, (375, 525, 150, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    medium_game_modes_surface = game_modes_font.render(game_modes[1], 0, BUTTON_FONT_COLOR)
    medium_game_modes_rect = medium_game_modes_surface.get_rect(center=(width / 2, height / 2 + 100))
    screen.blit(medium_game_modes_surface, medium_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button

    pygame.draw.rect(screen, BUTTON_COLOR, (600, 525, 100, 50))
    # this rectangle creates a fill with the secondary color
    pygame.draw.rect(screen, BUTTON_OUTLINE_COLOR, (600, 525, 100, 50), 3)
    # this rectangle creates an outline with a width of 3 pixels
    hard_game_modes_surface = game_modes_font.render(game_modes[2], 0, BUTTON_FONT_COLOR)
    hard_game_modes_rect = hard_game_modes_surface.get_rect(center=(width / 2 + 200, height / 2 + 100))
    screen.blit(hard_game_modes_surface, hard_game_modes_rect)
    # the font is rendered and placed on the screen above the rectangles to create a button
