import pygame
import numpy as np
import sys
import TaxiDriver



WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CIANO = (0, 255, 255)
BLACK = (0, 0, 0)


CELL_SIZE = 50
# NUM_COLS = int(input('DIgite o numero de colunas desejadas :'))
# NUM_ROWS = int(input('DIgite o numero de linhas desejadas :'))
NUM_COLS = 5
NUM_ROWS = 5
board = np.zeros((NUM_ROWS, NUM_COLS))


pygame.init()

WINDOW_SIZE = (NUM_COLS * CELL_SIZE, NUM_ROWS * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pinte o Tabuleiro")

state = ''

def getLista(array):
    lista = []
    for i in range(len(array[0])) :
            lista.append([array[0][i], array[1][i]])
    return lista

teste = True
while teste:



    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN and  (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
            state = 'pronto'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique do mouse
            x, y = event.pos
            # Calcula a posição do quadrado clicado
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            
            # Pinta o quadrado clicado


            if board[row][col] == 0:
                board[row][col] = 1
            else :
                board[row][col] = 0


            # if board[row][col] != 1:
            
            #     old_cord = np.where(board == 2)
            #     board[old_cord] = 0
                

    # Desenha o tabuleiro na tela
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 2:
                pygame.draw.rect(screen, CIANO, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))             

    for i in range(1,NUM_COLS):
        pygame.draw.line(screen, color=BLACK, start_pos=(WINDOW_SIZE[0]//NUM_COLS*i,0), end_pos= (WINDOW_SIZE[0]//NUM_COLS*i,WINDOW_SIZE[1]))
    for i in range(1,NUM_ROWS):
        pygame.draw.line(screen, color=BLACK, start_pos=(0, WINDOW_SIZE[1]//NUM_ROWS*i), end_pos= (WINDOW_SIZE[0], WINDOW_SIZE[1]//NUM_ROWS*i))




    # Atualiza a tela
    pygame.display.update()



    if state == 'pronto' :

        obstaculos_array = np.where(board == 1)
        taxi_array = np.where(board == 2)
        passageiro_array = np.where(board == 3)
        objetivo_array = np.where(board == 4)
        taxi_com_passageiro_array = np.where(board == 5)

        obstaculos_lista = getLista(obstaculos_array)
        taxi_lista = getLista(taxi_array)
        objetivo_lista = getLista(objetivo_array)
        passageiro_lista = getLista(passageiro_array)
        taxi_com_passageiro_lista = getLista(taxi_com_passageiro_array)

        teste = False
        

a = TaxiDriver.main([NUM_ROWS,NUM_COLS], taxi_lista[0], obstaculos_lista, passageiro_lista[0], objetivo_lista[0])

print (a)











