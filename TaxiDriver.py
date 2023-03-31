from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State
import random

def cria_exemplo(dimensao):
    taxi = [random.randint(0,dimensao-1), random.randint(0,dimensao-1)]
    passageiro = [random.randint(0,dimensao-1), random.randint(0,dimensao-1)]
    destino = [random.randint(0,dimensao-1), random.randint(0,dimensao-1)]
    obstaculos = []
    qtd_obstaculos = random.randint(0,dimensao*dimensao)
    for i in range(qtd_obstaculos):
        obstaculos.append([random.randint(0,dimensao-1), random.randint(0,dimensao-1)])
    return [dimensao, dimensao], taxi, obstaculos, passageiro, destino





class Taxi(State):

    def __init__(self,op, mapa_dimensao, taxi, obstaculos, passageiro, destino, carro_com_passageiro=False):
        self.mapa_dimensao = mapa_dimensao
        self.operator = op
        self.taxi = taxi
        self.obstaculos = obstaculos
        self.passageiro = passageiro
        self.destino = destino
        self.carro_com_passageiro = carro_com_passageiro
    
    def sucessors(self):
        sucessors = []
        if self.taxi[0] > 0 and [self.taxi[0]-1,self.taxi[1]] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("cima", self.mapa_dimensao,[self.taxi[0]-1, self.taxi[1]], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("cima", self.mapa_dimensao,[self.taxi[0]-1, self.taxi[1]], self.obstaculos, [self.taxi[0]-1, self.taxi[1]], self.destino, self.carro_com_passageiro))


        if self.taxi[0] < self.mapa_dimensao[0]-1 and [self.taxi[0]+1,self.taxi[1]] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("baixo", self.mapa_dimensao,[self.taxi[0]+1, self.taxi[1]], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("baixo", self.mapa_dimensao,[self.taxi[0]+1, self.taxi[1]], self.obstaculos, [self.taxi[0]+1, self.taxi[1]], self.destino, self.carro_com_passageiro))


        if self.taxi[1] > 0 and [self.taxi[0],self.taxi[1]-1] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("esquerda", self.mapa_dimensao,[self.taxi[0], self.taxi[1]-1], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("esquerda", self.mapa_dimensao,[self.taxi[0], self.taxi[1]-1], self.obstaculos, [self.taxi[0], self.taxi[1]-1], self.destino, self.carro_com_passageiro))

        if self.taxi[1] < self.mapa_dimensao[1]-1 and [self.taxi[0],self.taxi[1]+1] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("direita", self.mapa_dimensao,[self.taxi[0], self.taxi[1]+1], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("direita", self.mapa_dimensao,[self.taxi[0], self.taxi[1]+1], self.obstaculos, [self.taxi[0], self.taxi[1]+1], self.destino, self.carro_com_passageiro))


        if self.taxi == self.passageiro and self.carro_com_passageiro == False:
            sucessors.append(Taxi("pegar passageiro", self.mapa_dimensao, self.taxi, self.obstaculos, self.passageiro, self.destino, True))

        if self.taxi == self.passageiro and self.carro_com_passageiro == True:
            sucessors.append(Taxi("deixar passageiro", self.mapa_dimensao, self.taxi, self.obstaculos, self.passageiro, self.destino, False))

        return sucessors

    def is_goal(self):
        return (self.passageiro == self.destino and self.carro_com_passageiro==False)

    def description(self):
        return "Um algoritmo que resolve o problema do TaxiDriver"
    
    def h(self):
        if self.carro_com_passageiro == False:
            soma = abs(self.taxi[0] - self.passageiro[0]) + abs(self.taxi[1] - self.passageiro[1])
        else:
            soma = abs(self.taxi[0] - self.destino[0]) + abs(self.taxi[1] - self.destino[1])
        return soma


    def show_path(self):
        state = Taxi(self.operator, self.mapa_dimensao, self.taxi, self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro)
        algorithm = AEstrela()
        result = algorithm.search(state, trace=True)
        if result == None:
            print('Nao achou solucao')
            return 'Nao achou solucao'
        print(result.show_path())
        return result
    
    def env(self):
        return str(self.operator) + str(self.taxi) + str(self.carro_com_passageiro) + str(self.passageiro)
    
    def cost(self):
        if "passageiro" in self.operator:
            return 5
        else:
            return 1

def main():
    dimensao, taxi, obstaculos, passageiro, destino = cria_exemplo(15 )
    state = Taxi("", dimensao, [0,0], [], [dimensao[0]-1,dimensao[0]-1], [0,0])
    algorithm = AEstrela()
    result = algorithm.search(state, trace=True)
    if result == None:
        print('Nao achou solucao')
        return 'Nao achou solucao'
    print(result.show_path())
    return result

if __name__ == '__main__':
    main()