import numpy as np
import copy

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


path = "; esquerda ; baixo ; cima ; direita"

board = np.array([[ 0, 0, 0],[0, 1, 0],[0, 0,0,]])

print (gerar_boards(path, board))
      