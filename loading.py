import pygame
import sys
import numpy as np

import pygame
import sys

def load_game_of_life(screen):
    # Initialisation de Pygame
    pygame.init()

    # Dimensions de la fenêtre
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 830

    # Charger l'image de fond
    background_image = pygame.image.load("conway.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_rect = background_image.get_rect()
    background_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Police de caractères pour le texte
    font = pygame.font.SysFont('Hubot Sans', 50)

    # Texte "Appuyez sur Entrer pour continuer"
    enter_text = font.render("Appuyez sur Entrer pour continuer", True, WHITE)
    enter_rect = enter_text.get_rect()
    enter_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 370)

    # Créer une animation de points tournants
    point_size = 10
    point_color = WHITE
    points = [
        [SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2 + 30, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30],
        [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50]
    ]
    angle = 0
    rotation_speed = 5
    point_speed = 3
    running = True


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
        #screen.fill(BLACK)

        # Affichage d'une animation
        time = pygame.time.get_ticks()  # Récupération du temps écoulé depuis le début de la boucle
        angle = np.sin(time / 1000) * 45  # Calcul de l'angle de rotation en fonction du temps
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 50, 80, 80))  # Dessin d'un carré blanc
        rotated_rect = pygame.transform.rotate(background_image, angle)  # Rotation du carré
        screen.blit(rotated_rect, rotated_rect.get_rect(center=background_rect.center)) # Affichage du carré

        # Affichage des textes
        screen.blit(enter_text, enter_rect)

        # Rafraîchissement de l'écran
        pygame.display.flip()
