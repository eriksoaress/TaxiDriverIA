import pygame
import numpy as np
import sys

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CELL_SIZE = 50
NUM_COLS = int(input('DIgite o numero de colunas desejadas :'))
NUM_ROWS = int(input('DIgite o numero de linhas desejadas :'))
WINDOW = 'obstaculos'
FASE = 0
board = np.zeros((NUM_ROWS, NUM_COLS))

pygame.init()

WINDOW_SIZE = (NUM_COLS * CELL_SIZE, NUM_ROWS * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TaxiGame")
