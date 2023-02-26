import time
import pygame
import numpy as np

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


def penta(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer la ruche
    penta_coords = [(0, -4), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    
    for coord in penta_coords:
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


def t_bordel(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le serpent
    bordel_coords = [(0, 2), (0, 3), (1, 1), (1, 2), (2, 2)]
    
    for coord in bordel_coords:
        cells[y + coord[0], x + coord[1]] = 1


def heart(cells):
    pos = pygame.mouse.get_pos()
    x = pos[0] // 10
    y = pos[1] // 10
    
    # Placer le coeur
    heart_coords = [(0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18),                     (1, 4), (1, 5), (1, 9), (1, 13), (1, 14), (1, 18), (2, 3), (2, 4), (2, 9), (2, 10),                     (2, 11), (2, 12), (2, 17), (2, 18), (3, 2), (3, 3), (3, 10), (3, 16), (3, 17), (4, 1),                     (4, 2), (4, 10), (4, 15), (4, 16), (5, 0), (5, 1), (5, 10), (5, 14), (5, 15), (6, 1),                     (6, 2), (6, 10), (6, 13), (6, 14), (7, 2), (7, 3), (7, 9), (7, 12), (7, 13), (8, 3),                     (8, 4), (8, 9), (8, 11), (8, 12), (9, 4), (9, 5), (9, 9), (9, 10), (9, 11), (10, 5),                     (10, 6), (10, 7), (10, 8), (10, 9)]
    
    for coord in heart_coords:
        cells[y + coord[0], x + coord[1]] = 1

