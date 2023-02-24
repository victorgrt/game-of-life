import pygame
import sys
import numpy as np

def load_game_of_life(screen):
    # Initialisation de Pygame
    pygame

    # Dimensions de la fenêtre
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 830

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Police de caractères pour le texte
    font = pygame.font.SysFont('Hubot Sans', 50)

    # Texte "Game of Life"
    title_text = font.render("Game of Life", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

    # Texte "Appuyez sur Entrer pour continuer"
    enter_text = font.render("Appuyez sur Entrer pour continuer", True, GRAY)
    enter_rect = enter_text.get_rect()
    enter_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    # Boucle principale
    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_RETURN:
                    running = False
                    # L'utilisateur a appuyé sur Entrer, on quitte la boucle
                    return
                elif Q.key == pygame.K_q or Q.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Fond noir
        screen.fill(BLACK)

        # Affichage des textes
        screen.blit(title_text, title_rect)
        screen.blit(enter_text, enter_rect)

        # Rafraîchissement de l'écran
        pygame.display.flip()
