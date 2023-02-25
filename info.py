import pygame
import numpy as np
import time

GREEN = (0, 197, 84)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 830

def display_rules(screen):

    font = pygame.font.SysFont('Arial', 50)
    title_text = font.render("Infos :", True, GREEN)
    title_rect = title_text.get_rect()
    screen.fill(BLACK)
    screen.blit(title_text, (50, 50))

    # Création de la liste des options
    options = ["① - Glider", "② - Pulsar", "③ - Clignotant", "④ - Gosper Glider Gun",
               "⑤ - Beehive", "⑥ - Spaceship", "⑦ - T", "⑧ - Heart", "⑨ - Penta"]

    # Affichage des options
    option_font = pygame.font.SysFont('Arial', 30)
    option_spacing = 60
    for i, option in enumerate(options):
        option_text = option_font.render(option, True, WHITE)
        option_rect = option_text.get_rect()
        option_rect.x = 50
        option_rect.y = 120 + (i * option_spacing)
        screen.blit(option_text, option_rect)

    pygame.display.flip()
