import pygame
import sys
import numpy as np
import copy

CELL_SIZE = 50

def obstaculos(board, window):
    l = [2,3,4,5]
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
            if board[row][col] not in l and board[row][col] == 1:
                board[row][col] = 0
            elif board[row][col] not in l and board[row][col] == 0:
                board[row][col] = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window = 'taxi'
    return board,window

def taxi(board, window):
    l = [1,4]
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
            if 5 in board:
                old_cord = np.where(board == 5)
                if board[old_cord][0] != board[row,col] and board[row,col] not in l:
                    board[old_cord] = 3
                    board[row][col] = 2
            elif board[row][col] == 3:
                old_cord = np.where(board == 2)
                board[old_cord] = 0
                board[row][col] = 5
            elif board[row][col] != 1:
                old_cord = np.where(board == 2)
                board[old_cord] = 0
                board[row][col] = 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window = 'passageiro'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                window = 'obstaculos'
    return board,window

def passageiro(board,window):
    l = [1,4]
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
            if 5 in board:
                old_cord = np.where(board == 5)
                if board[old_cord][0] != board[row,col] and board[row,col] not in l:
                    board[old_cord] = 2
                    board[row][col] = 3
            #Caso tente colocar o passsageiro junto do taxi
            elif board[row][col] == 2:
                old_cord = np.where(board == 3)
                board[old_cord] = 0
                board[row][col] = 5
            elif board[row][col] != 1:
                old_cord = np.where(board == 3)
                board[old_cord] = 0
                board[row][col] = 3
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window = 'objetivo'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                window = 'taxi'
    return board, window

def objetivo(board, window, FASE = 0):
    l = [1,2,3,4,5]
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
            if board[row][col] not in l:
                old_cord = np.where(board == 4)
                board[old_cord] = 0
                board[row][col] = 4
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window = 'animacao'
                FASE = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                window = 'passageiro'
        
    return board, window, FASE

#################################################################################################################################################
def getLista(array):
    lista = []
    for i in range(len(array[0])) :
            lista.append([array[0][i], array[1][i]])
    return lista



def gerar_boards (path, board_inicial):
    path_sem_espaco = path.replace(" ", "")
    path_lista = []
    for etapa in path_sem_espaco.split(';'):
        path_lista.append(etapa)


    boards = [board_inicial]

    for i in path_lista :
        novo_board = copy.deepcopy(boards[len(boards)-1])
        taxi_array = np.where(novo_board == 2)
        taxi = getLista(taxi_array)[0]

        if i == "direita" :

            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]][taxi[1]+1] = 2
            boards.append(novo_board)
        if i == "esquerda" :

            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]][taxi[1]-1] = 2
            boards.append(novo_board)
        if i == "baixo" :

            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]+1][taxi[1]] = 2
            boards.append(novo_board)
        if i == "cima" :

            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]-1][taxi[1]] = 2
            boards.append(novo_board)



            
    # return [board.tolist() for board in boards]
    return boards

def animacao(board, n):
    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if n> len(board) -2:
                    n = 0
                n += 1
            elif event.key == pygame.K_LEFT:
                n -= 1

        
    
    board = board[n]
    return board, n





    




