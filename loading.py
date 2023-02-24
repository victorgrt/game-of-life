import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 830

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game of Life")

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
                # L'utilisateur a appuyé sur Entrer, on quitte la boucle
                break
    
    # Fond noir
    screen.fill(BLACK)
    
    # Affichage des textes
    screen.blit(title_text, title_rect)
    screen.blit(enter_text, enter_rect)
    
    # Rafraîchissement de l'écran
    pygame.display.flip()
