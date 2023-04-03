from functionsGame import *
import pygame
import numpy as np
import sys
import TaxiDriver

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (65,105,225)
CIANO = (173,216,230)
PINK = (255,20,147)
BLACK = (0, 0, 0)
GREEN = (60,179,113)
PURPLE = (139,0,139)
YELLOW = (255, 255, 0)
NUM_COLS = int(input('Digite o numero de colunas desejadas :'))
NUM_ROWS = int(input('Digite o numero de linhas desejadas :'))
if NUM_COLS > NUM_ROWS:
    CELL_SIZE = int(800/NUM_COLS)
else:
    CELL_SIZE = int(800/NUM_ROWS)
window = 'obstaculos'
FASE = 0
board = np.zeros((NUM_ROWS, NUM_COLS))
C_HEIGHT = CELL_SIZE*NUM_ROWS
C_WIDTH = CELL_SIZE*NUM_COLS
CDIMENSOES = [C_WIDTH,C_HEIGHT]
SIDE_BAR_WIDTH = 300

pygame.init()

WINDOW_SIZE = (800,800)
WINDOW_W_BAR_SIZE = (1100, 800)
screen = pygame.display.set_mode(WINDOW_W_BAR_SIZE)
pygame.display.set_caption("TaxiGame")
# Criar a superfície da barra lateral
    
side_bar = pygame.Surface((SIDE_BAR_WIDTH, 800))

# Desenhar os botões na barra lateral
button_font = pygame.font.Font(None, 30)
l_colors = [BLUE,YELLOW,CIANO,PURPLE,BLACK]
l_colors_text = [WHITE,BLACK,BLACK,WHITE,WHITE]
button_rects = []
button_dict = {}
for i, button_text in enumerate(["obstaculos", "taxi", "passageiro", "destino", "começar"]):
    button_rect = pygame.draw.rect(screen, l_colors_text[i], (850, 150 + i * 100, 200, 50))
    button_surface = button_font.render(button_text, True, l_colors_text[i])
    button_rect_center = button_surface.get_rect(center=button_rect.center)
    button_rects.append(button_rect)
    button_dict[i] = [button_rect_center,button_surface,(850, 150 + i * 100, 200, 50)]
    # Posicionar a barra lateral na lateral direita da tela


while FASE == 0:

    side_bar.fill(WHITE)
    screen.blit(side_bar, (WINDOW_W_BAR_SIZE[0] - SIDE_BAR_WIDTH, 0))

    if window == 'obstaculos':
        board,window = obstaculos(board, window,CELL_SIZE,button_rects,CDIMENSOES)
    elif window == 'taxi':
        board,window = taxi(board, window,CELL_SIZE,button_rects,CDIMENSOES)
    elif window == 'passageiro':
        board,window = passageiro(board, window,CELL_SIZE,button_rects,CDIMENSOES)
    elif window == 'objetivo':
        board,window, FASE = objetivo(board,window,CELL_SIZE,button_rects,CDIMENSOES)
    elif window == 'animacao':
        FASE = 1

    

     # Desenha o tabuleiro na tela
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 2:
                pygame.draw.rect(screen, YELLOW, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 3:
                pygame.draw.rect(screen, CIANO, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 4:
                pygame.draw.rect(screen, PURPLE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 5:
                pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 6:
                pygame.draw.rect(screen, PINK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))             

    for i in range(1,NUM_COLS+1):
        pygame.draw.line(screen, color=BLACK, start_pos=(CELL_SIZE*i,0), end_pos= (CELL_SIZE*i,WINDOW_SIZE[1]))
    for i in range(0,NUM_ROWS):
        pygame.draw.line(screen, color=BLACK, start_pos=(0, CELL_SIZE*i), end_pos= (WINDOW_SIZE[0], CELL_SIZE*i))

    for i, button_prop in button_dict.items():
        button_rect = pygame.draw.rect(screen, l_colors[i], button_prop[2])
        screen.blit(button_prop[1], button_prop[0])
        
    
    # Atualiza a tela
    pygame.display.update()

# Rodar taxi driver devolve o path ----------------------

obstaculos_array = np.where(board == 1)
taxi_array = np.where(board == 2)
passageiro_array = np.where(board == 3)
objetivo_array = np.where(board == 4)
taxi_com_passageiro_array = np.where(board == 5)
taxi_no_destino = np.where(board == 6)

obstaculos_lista = getLista(obstaculos_array)
taxi_lista = getLista(taxi_array)
objetivo_lista = getLista(objetivo_array)
passageiro_lista = getLista(passageiro_array)
taxi_com_passageiro_lista = getLista(taxi_com_passageiro_array)
taxi_no_destino_lista = getLista(taxi_no_destino)
n_taxi = 0
if 5 not in board:
    if 6 in board:
        path = TaxiDriver.main([NUM_ROWS,NUM_COLS], taxi_no_destino_lista[0], obstaculos_lista, passageiro_lista[0], taxi_no_destino_lista[0]).show_path()
        n_taxi = 6
    else:
        path = TaxiDriver.main([NUM_ROWS,NUM_COLS], taxi_lista[0], obstaculos_lista, passageiro_lista[0], objetivo_lista[0]).show_path()
        n_taxi = 2
else:
    path = TaxiDriver.main([NUM_ROWS,NUM_COLS], taxi_com_passageiro_lista[0], obstaculos_lista, taxi_com_passageiro_lista[0], objetivo_lista[0],carro_com_passageiro =True).show_path()
    n_taxi = 5


n = 0
time = 0
boards = gerar_boards(path,board, n_taxi)
while FASE == 1:
    if window == 'animacao':
        
        board,n = animacao(boards, n)
    time += 1
    if time%120 == 0:
        if n<= len(boards) -2:
            n += 1

     # Desenha o tabuleiro na tela5
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 2:
                pygame.draw.rect(screen, YELLOW, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 3:
                pygame.draw.rect(screen, CIANO, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 4:
                pygame.draw.rect(screen, PURPLE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 5:
                pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[row][col] == 6:
                pygame.draw.rect(screen, PINK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))             

    # for i in range(1,NUM_COLS):
    #     pygame.draw.line(screen, color=BLACK, start_pos=(WINDOW_SIZE[0]//NUM_COLS*i,0), end_pos= (WINDOW_SIZE[0]//NUM_COLS*i,WINDOW_SIZE[1]))
    # for i in range(1,NUM_ROWS):
    #     pygame.draw.line(screen, color=BLACK, start_pos=(0, WINDOW_SIZE[1]//NUM_ROWS*i), end_pos= (WINDOW_SIZE[0], WINDOW_SIZE[1]//NUM_ROWS*i))
    for i in range(1,NUM_COLS+1):
        pygame.draw.line(screen, color=BLACK, start_pos=(CELL_SIZE*i,0), end_pos= (CELL_SIZE*i,WINDOW_SIZE[1]))
    for i in range(0,NUM_ROWS):
        pygame.draw.line(screen, color=BLACK, start_pos=(0, CELL_SIZE*i), end_pos= (WINDOW_SIZE[0], CELL_SIZE*i))
    # Atualiza a tela
    pygame.display.update()

