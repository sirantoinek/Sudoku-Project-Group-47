import pygame
from constants import *


class Victory:
    def __init__(self, s):
        self.secret = s
        w = pygame.image.load("Bamboo.jpg")
        self.secret.blit(w, (-100, 0))
        self.secret.blit(w, (-100, 300))

    def win(self):
        title_screen_font = pygame.font.Font(None, TITLE_FONT_SIZE)
        title_surface = title_screen_font.render("Victory!!!", 0, DEFAULT_FONT_COLOR)
        title_rect = title_surface.get_rect(center=(900 / 2, 200))
        self.secret.blit(title_surface, title_rect)
        title_screen_font = pygame.font.Font(None, 60)
        title_surface = title_screen_font.render("Press enter to return to menu.", 0, DEFAULT_FONT_COLOR)
        title_rect = title_surface.get_rect(center=(900 / 2, 500))
        self.secret.blit(title_surface, title_rect)

    def loss(self):
        title_screen_font = pygame.font.Font(None, TITLE_FONT_SIZE)
        title_surface = title_screen_font.render("You Lose.", 0, DEFAULT_FONT_COLOR)
        title_rect = title_surface.get_rect(center=(900 / 2, 200))
        self.secret.blit(title_surface, title_rect)
        title_screen_font = pygame.font.Font(None, 60)
        title_surface = title_screen_font.render("Press enter to return to menu.", 0, DEFAULT_FONT_COLOR)
        title_rect = title_surface.get_rect(center=(900 / 2, 500))
        self.secret.blit(title_surface, title_rect)
