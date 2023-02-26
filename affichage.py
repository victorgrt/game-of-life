import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10)
COLOR_GRID = (0, 177, 64)
COLOR_DIE_NEXT = (0,157, 44)
COLOR_ALIVE_NEXT = (0, 197, 84)
COLOR_TEXT = (255, 255, 255)

def display_rules(screen):

    GREEN = (0, 197, 84)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

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

def display_info(screen, generation, alive_cells, dead_cells):
    font = pygame.font.SysFont("Hubot Sans", 40)
    text_generation = font.render("Generation: " + str(generation), True, COLOR_TEXT)
    text_alive = font.render("Alive cells: " + str(alive_cells), True, COLOR_TEXT)
    text_dead = font.render("Dead cells: " + str(dead_cells), True, COLOR_TEXT)
    text_info = font.render("Press R for infos", True, COLOR_TEXT)

    screen.blit(text_generation, (10, 800))
    screen.blit(text_alive, (260, 800))
    screen.blit(text_dead, (520, 800))
    screen.blit(text_info, (780, 800))

    pygame.display.update()

