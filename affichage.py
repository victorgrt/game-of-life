import time
import pygame
import numpy as np

def display_patterns(screen):
    # Dimensions de la fenêtre
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 830

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Police de caractères pour le texte
    font = pygame.font.SysFont('Hubot Sans', 50)

    # Texte "Patterns"
    patterns_text = font.render('''Pour directement faire spawn un de ces patterns, appuyez sur la touche correspondante''', True, WHITE)
    patterns_rect = patterns_text.get_rect()
    patterns_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 300)

    # Texte des différents patterns
    pattern_1_text = font.render("1 - Glider", True, WHITE)
    pattern_1_rect = pattern_1_text.get_rect()
    pattern_1_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 250)

    pattern_2_text = font.render("2 - Pulsar", True, WHITE)
    pattern_2_rect = pattern_2_text.get_rect()
    pattern_2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)

    pattern_3_text = font.render("3 - Clignotant", True, WHITE)
    pattern_3_rect = pattern_3_text.get_rect()
    pattern_3_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

    pattern_4_text = font.render("4 - Gosper Glider Gun", True, WHITE)
    pattern_4_rect = pattern_4_text.get_rect()
    pattern_4_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    pattern_5_text = font.render("5 - Behive", True, WHITE)
    pattern_5_rect = pattern_5_text.get_rect()
    pattern_5_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)

    pattern_6_text = font.render("6 - Middle Weight Spaceship", True, WHITE)
    pattern_6_rect = pattern_6_text.get_rect()
    pattern_6_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
    
    pattern_7_text = font.render("7 - Serpent", True, WHITE)
    pattern_7_rect = pattern_7_text.get_rect()
    pattern_7_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 350)

    pattern_8_text = font.render("8 - Heart", True, WHITE)
    pattern_8_rect = pattern_8_text.get_rect()
    pattern_8_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 450)

    # Boucle principale
    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_RETURN:
                    # L'utilisateur a appuyé sur Entrer, on quitte la boucle
                    return
                elif Q.key == pygame.K_q or Q.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Fond noir
        screen.fill(BLACK)

        # Affichage des textes
        screen.blit(patterns_text, patterns_rect)
        screen.blit(pattern_1_text, pattern_1_rect)
        screen.blit(pattern_2_text, pattern_2_rect)
        screen.blit(pattern_3_text, pattern_3_rect)
        screen.blit(pattern_4_text, pattern_4_rect)
        screen.blit(pattern_5_text, pattern_5_rect)
        screen.blit(pattern_6_text, pattern_6_rect)
        screen.blit(pattern_7_text, pattern_7_rect)
        screen.blit(pattern_8_text, pattern_8_rect)

        # Rafraîchissement de l'écran
        pygame.display.flip()
