import pygame
import sys
import numpy as np
import copy


def obstaculos(board, window,CELL_SIZE,button_rects,CDIMENSOES):
    l_buttons = ["obstaculos", "taxi", "passageiro", "destino", "começar"]
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
            if (x>0 and x <CDIMENSOES[0]) and (y>0 and y<CDIMENSOES[1]):
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                # Pinta o quadrado clicado
                if board[row][col] not in l and board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] not in l and board[row][col] == 0:
                    board[row][col] = 1
            # Verificar se o clique foi em um botão
            elif (x<1100 and x > 800):
                window = click_botoes(button_rects,l_buttons,window,event.pos)
    return board,window


def click_botoes(button_rects, l_buttons, window,pos_event):
    for i, button_rect in enumerate(button_rects):
        if button_rect.collidepoint(pos_event):
            botao = l_buttons[i]
            if botao == "obstaculos":
                window = "obstaculos"
            elif botao == "taxi":
                window = "taxi"
            elif botao == "passageiro":
                window = "passageiro"
            elif botao == "destino":
                window = "objetivo"
            elif botao == "começar":
                window = "animacao"
            print("Botão", l_buttons[i], "clicado")
            print(window)
    return window

def taxi(board, window, CELL_SIZE, button_rects,CDIMENSOES):
    l_buttons = ["obstaculos", "taxi", "passageiro", "destino", "começar"]
    l = [1]
    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique do mouse
            x, y = event.pos
            if (x>0 and x <CDIMENSOES[0]) and (y>0 and y<CDIMENSOES[1]):
                # Calcula a posição do quadrado clicado
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                # Pinta o quadrado clicado
                if 5 in board:
                    old_cord = np.where(board == 5)
                    if board[old_cord][0] != board[row,col] and board[row,col] not in l:
                        board[old_cord] = 3
                        board[row][col] = 2
                elif 6 in board:
                    old_cord = np.where(board == 6)
                    if board[old_cord][0] != board[row,col] and board[row,col] != 1:
                        board[old_cord] = 4
                        board[row][col] = 2
                elif board[row][col] == 3:
                    old_cord = np.where(board == 2)
                    board[old_cord] = 0
                    board[row][col] = 5
                elif board[row][col] == 4:
                    old_cord = np.where(board == 2)
                    board[old_cord] = 0
                    board[row][col] = 6
                elif board[row][col] != 1:
                    old_cord = np.where(board == 2)
                    board[old_cord] = 0
                    board[row][col] = 2
            elif (x<1100 and x > 800):
                window = click_botoes(button_rects,l_buttons,window,event.pos)
    return board,window

def passageiro(board,window, CELL_SIZE,button_rects,CDIMENSOES):
    l_buttons = ["obstaculos", "taxi", "passageiro", "destino", "começar"]
    l = [1,4]
    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique do mouse
            x, y = event.pos
            if (x>0 and x <CDIMENSOES[0]) and (y>0 and y<CDIMENSOES[1]):
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
                elif board[row][col] not in l:
                    old_cord = np.where(board == 3)
                    board[old_cord] = 0
                    board[row][col] = 3
            elif (x<1100 and x > 800):
                window = click_botoes(button_rects,l_buttons,window,event.pos)
    return board, window

def objetivo(board, window, CELL_SIZE, button_rects,CDIMENSOES,FASE = 0):
    l_buttons = ["obstaculos", "taxi", "passageiro", "destino", "começar"]
    l = [1,2,3,4,5]
    # Lida com eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique do mouse
            x, y = event.pos
            if (x>0 and x <CDIMENSOES[0]) and (y>0 and y<CDIMENSOES[1]):
                # Calcula a posição do quadrado clicado
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                # Pinta o quadrado clicado
                if 6 in board:
                    old_cord = np.where(board == 6)
                    if board[old_cord][0] != board[row,col] and board[row,col] != 1:
                        board[old_cord] = 2
                        board[row][col] = 4
                elif board[row][col] == 2:
                    old_cord = np.where(board == 4)
                    board[old_cord] = 0
                    board[row][col] = 6
                elif board[row][col] not in l:
                    old_cord = np.where(board == 4)
                    board[old_cord] = 0
                    board[row][col] = 4
            elif (x<1100 and x > 800):
                window = click_botoes(button_rects,l_buttons,window,event.pos)
        
    return board, window, FASE

#################################################################################################################################################
def getLista(array):
    lista = []
    for i in range(len(array[0])) :
            lista.append([array[0][i], array[1][i]])
    return lista



def gerar_boards (path, board_inicial, n_taxi):
    path_sem_espaco = path.replace(" ", "")
    path_lista = []
    for etapa in path_sem_espaco.split(';'):
        path_lista.append(etapa)


    boards = [board_inicial]
    print(path_lista)
    for i in path_lista :
        novo_board = copy.deepcopy(boards[len(boards)-1])
        taxi_array = np.where(novo_board == n_taxi)
        taxi = getLista(taxi_array)[0]

        if i == "direita" :
            a = novo_board[taxi[0]][taxi[1]]
            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]][taxi[1]+1] = n_taxi
            boards.append(novo_board)
        if i == "esquerda" :
            a= novo_board[taxi[0]][taxi[1]]
            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]][taxi[1]-1] = n_taxi
            boards.append(novo_board)
        if i == "baixo" :
            a = novo_board[taxi[0]][taxi[1]]
            novo_board[taxi[0]][taxi[1]] = 0 
            novo_board[taxi[0]+1][taxi[1]] = n_taxi
            boards.append(novo_board)
        if i == "cima" :
            a = novo_board[taxi[0]][taxi[1]]
            novo_board[taxi[0]][taxi[1]] = 0
            novo_board[taxi[0]-1][taxi[1]] = n_taxi
            boards.append(novo_board)

        if i == "pegarpassageiro":
            n_taxi = 5
            novo_board[taxi[0]][taxi[1]] = n_taxi
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
                    n = -1
                n += 1
            elif event.key == pygame.K_LEFT:
                if n<= -len(board)+1 :
                    n = 1
                n -= 1

        
    
    board = board[n]
    return board, n





    




