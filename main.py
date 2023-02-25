import time
from affichage import display_patterns
from loading import load_game_of_life
import pygame
import numpy as np

COLOR_BG = (10, 10, 10)
COLOR_GRID = (0, 177, 64)
COLOR_DIE_NEXT = (0,157, 44)
COLOR_ALIVE_NEXT = (0, 197, 84)
COLOR_TEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("THE GAME OF LIFE")

def count_dead_cells(cells):
    return np.sum(cells == 0)

def display_info(screen, generation, alive_cells, dead_cells):
    font = pygame.font.SysFont("Hubot Sans", 40)
    text_generation = font.render("Generation: " + str(generation), True, COLOR_TEXT)
    text_alive = font.render("Alive cells: " + str(alive_cells), True, COLOR_TEXT)
    text_dead = font.render("Dead cells: " + str(dead_cells), True, COLOR_TEXT)

    screen.blit(text_generation, (10, 800))
    screen.blit(text_alive, (260, 800))
    screen.blit(text_dead, (520, 800))

    pygame.display.update()

def glider(cells):
    pos = pygame.mouse.get_pos()
    cells[pos[1] // 10, pos[0] // 10 + 1] = 1
    cells[pos[1] // 10 + 1, pos[0] // 10 + 2] = 1
    cells[pos[1] // 10 + 2, pos[0] // 10] = 1
    cells[pos[1] // 10 + 2, pos[0] // 10 + 1] = 1
    cells[pos[1] // 10 + 2, pos[0] // 10 + 2] = 1

def gosper_glider_gun(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    # première rangée
    cells[y, x+24] = 1
    cells[y+1, x+22] = 1
    cells[y+1, x+24] = 1
    cells[y+2, x+12] = 1
    cells[y+2, x+13] = 1
    cells[y+2, x+20] = 1
    cells[y+2, x+21] = 1
    cells[y+2, x+34] = 1
    cells[y+2, x+35] = 1

    # deuxième rangée
    cells[y+3, x+11] = 1
    cells[y+3, x+15] = 1
    cells[y+3, x+20] = 1
    cells[y+3, x+21] = 1
    cells[y+3, x+34] = 1
    cells[y+3, x+35] = 1
    # troisième rangée
    cells[y+4, x] = 1
    cells[y+4, x+1] = 1
    cells[y+4, x+10] = 1
    cells[y+4, x+16] = 1
    cells[y+4, x+20] = 1
    cells[y+4, x+21] = 1
    cells[y+5, x] = 1
    cells[y+5, x+1] = 1
    cells[y+5, x+10] = 1
    cells[y+5, x+14] = 1
    cells[y+5, x+16] = 1
    cells[y+5, x+17] = 1
    cells[y+5, x+22] = 1
    cells[y+5, x+24] = 1
    
    cells[y+6, x+10] = 1
    cells[y+6, x+16] = 1
    cells[y+6, x+24] = 1
    
    cells[y+7, x+11] = 1
    cells[y+7, x+15] = 1
    
    # quatrième rangée
    cells[y+8, x+12] = 1
    cells[y+8, x+13] = 1

def clignotant(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10

    clignotant_coords = [(1, 1), (1, 2), (1, 3)]

    for coord in clignotant_coords:
        cells[y + coord[0], x + coord[1]] = 1

def pulsar(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le pulsar
    pulsar_coords = [(0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10), (2, 0), (3, 0), (4, 0), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 7), (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10), (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10), (8, 5), (9, 5), (10, 5), (8, 7), (9, 7), (10, 7), (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10), (14, 0), (15, 0), (16, 0), (14, 5), (15, 5), (16, 5), (14, 7), (15, 7), (16, 7), (17, 2), (17, 3), (17, 4), (17, 8), (17, 9), (17, 10)]
    
    for coord in pulsar_coords:
        cells[y + coord[0], x + coord[1]] = 1

def beehive(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer la ruche
    beehive_coords = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]
    
    for coord in beehive_coords:
        cells[y + coord[0], x + coord[1]] = 1


def middleweight_spaceship(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le vaisseau
    spaceship_coords = [(0, 1), (0, 4), (1, 5), (2, 0), (2, 5), (3, 5), (4, 5)]
    
    for coord in spaceship_coords:
        cells[y + coord[0], x + coord[1]] = 1


def serpent(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le serpent
    serpent_coords = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5), (2, 6), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (4, 10), (4, 11), (5, 11), (5, 12), (5, 13), (6, 13), (6, 14), (6, 15), (7, 15), (7, 16), (7, 17), (8, 17), (8, 18), (8, 19)]
    
    for coord in serpent_coords:
        cells[y + coord[0], x + coord[1]] = 1


def heart(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le coeur
    heart_coords = [(0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18),                     (1, 4), (1, 5), (1, 9), (1, 13), (1, 14), (1, 18), (2, 3), (2, 4), (2, 9), (2, 10),                     (2, 11), (2, 12), (2, 17), (2, 18), (3, 2), (3, 3), (3, 10), (3, 16), (3, 17), (4, 1),                     (4, 2), (4, 10), (4, 15), (4, 16), (5, 0), (5, 1), (5, 10), (5, 14), (5, 15), (6, 1),                     (6, 2), (6, 10), (6, 13), (6, 14), (7, 2), (7, 3), (7, 9), (7, 12), (7, 13), (8, 3),                     (8, 4), (8, 9), (8, 11), (8, 12), (9, 4), (9, 5), (9, 9), (9, 10), (9, 11), (10, 5),                     (10, 6), (10, 7), (10, 8), (10, 9)]
    
    for coord in heart_coords:
        cells[y + coord[0], x + coord[1]] = 1



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
    display_patterns(screen)
    cells = np.zeros((80, 100))
    screen.fill(COLOR_BG)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False
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
                    serpent(cells)
                elif Q.key == pygame.K_8:
                    heart(cells)
                elif Q.key == pygame.K_q or Q.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
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
            dead_cells = count_dead_cells(cells)
            alive_cells = np.sum(cells == 1)

            if np.count_nonzero(cells) == 0:
                running = False

            display_info(screen, generation, np.count_nonzero(cells), dead_cells)
            pygame.display.update()
        
        #print(pygame.font.get_fonts())
        time.sleep(0.1)


if __name__ == "__main__":
    main()