import time
import pygame
import numpy as np

from loading import load_game_of_life
from affichage import display_rules
from affichage import display_info

from patterns import glider
from patterns import heart
from patterns import middleweight_spaceship
from patterns import clignotant
from patterns import serpent
from patterns import gosper_glider_gun
from patterns import beehive
from patterns import pulsar
from patterns import t_bordel
from patterns import penta

COLOR_BG = (10, 10, 10)
COLOR_GRID = (0, 177, 64)
COLOR_DIE_NEXT = (0,157, 44)
COLOR_ALIVE_NEXT = (0, 197, 84)
COLOR_TEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("THE GAME OF LIFE")

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 830))
    load_game_of_life(screen)
    cells = np.zeros((80, 100))
    screen.fill(COLOR_BG)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False
    displaying_rules = False
    generation = 0
    alive_cells = 0
    dead_cells = 0

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                elif Q.key == pygame.K_q or Q.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif Q.key == pygame.K_1:
                    glider(cells)
                elif Q.key == pygame.K_2:
                    pulsar(cells)
                elif Q.key == pygame.K_3:
                    clignotant(cells)
                elif Q.key == pygame.K_4:
                    gosper_glider_gun(cells) 
                elif Q.key == pygame.K_5:
                    beehive(cells)
                elif Q.key == pygame.K_6:
                    middleweight_spaceship(cells)
                elif Q.key == pygame.K_7:
                    t_bordel(cells)
                elif Q.key == pygame.K_8:
                    heart(cells)
                elif Q.key == pygame.K_9:
                    penta(cells)
                elif Q.key == pygame.K_r:
                    displaying_rules = not displaying_rules
                    

        if displaying_rules:
            running = False
            display_rules(screen)
        else:
            update(screen, cells, 10)
            pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    cells[(pos[1] // 10) + 1, pos[0] // 10] = 1
                    cells[(pos[1] // 10) - 1, pos[0] // 10] = 1
                    cells[pos[1] // 10, (pos[0] // 10) + 1] = 1
                    cells[pos[1] // 10, (pos[0] // 10) - 1] = 1
                else:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_BG)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            generation += 1
            dead_cells = 8000 - np.sum(cells == 0) + dead_cells
            alive_cells = np.sum(cells == 1)

            if np.count_nonzero(cells) == 0:
                running = False

            display_info(screen, generation, np.count_nonzero(cells), dead_cells)
            pygame.display.update()
        
        #print(pygame.font.get_fonts())
        time.sleep(0.1)


if __name__ == "__main__":
    main()