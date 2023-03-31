import pygame
import numpy as np
import sys



WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


CELL_SIZE = 50
NUM_COLS = int(input('DIgite o numero de colunas desejadas :'))
NUM_ROWS = int(input('DIgite o numero de linhas desejadas :'))

board = np.zeros((NUM_ROWS, NUM_COLS))


pygame.init()

WINDOW_SIZE = (NUM_COLS * CELL_SIZE, NUM_ROWS * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pinte o Tabuleiro")





while True:
    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique do mouse
            x, y = event.pos
            # Calcula a posição do quadrado clicado
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            
            # Pinta o quadrado clicado
            board[row][col] = 1
    
    # Desenha o tabuleiro na tela
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                

    for i in range(1,NUM_COLS):
        pygame.draw.line(screen, color=BLACK, start_pos=(WINDOW_SIZE[0]//NUM_COLS*i,0), end_pos= (WINDOW_SIZE[0]//NUM_COLS*i,WINDOW_SIZE[1]))
    for i in range(1,NUM_ROWS):
        pygame.draw.line(screen, color=BLACK, start_pos=(0, WINDOW_SIZE[1]//NUM_ROWS*i), end_pos= (WINDOW_SIZE[0], WINDOW_SIZE[1]//NUM_ROWS*i))
    # Atualiza a tela
    pygame.display.update()






