from TaxiDriver import Taxi
mapa_dimensao = [10,10] #dimensão do mapa
taxi = [0,0] # local do taxi
obstaculos = [[2,2],[3,3]] # locais dos obstaculos
passageiro = [5,5] # local do passageiro
destino = [6,9] # local do destino do passageiro
carro_com_passageiro = False # se o passageiro esta dentro do taxi ou nao

state = Taxi("", mapa_dimensao, taxi, obstaculos, passageiro, destino, carro_com_passageiro)
print(state.show_path().show_path())