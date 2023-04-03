from TaxiDriver import Taxi
mapa_dimensao = [10,10]
taxi = [0,0]
obstaculos = [[2,2],[3,3]]
passageiro = [5,5]
destino = [6,9]
carro_com_passageiro = False

state = Taxi("", mapa_dimensao, taxi, obstaculos, passageiro, destino, carro_com_passageiro)
print(state.show_path().show_path())