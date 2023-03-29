from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State

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
        if self.taxi[0] != 0 and [self.taxi[0]-1,self.taxi[1]] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("cima", self.mapa_dimensao,[self.taxi[0]-1, self.taxi[1]], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("cima", self.mapa_dimensao,[self.taxi[0]-1, self.taxi[1]], self.obstaculos, [self.taxi[0]-1, self.taxi[1]], self.destino, self.carro_com_passageiro))


        if self.taxi[0] != self.mapa_dimensao[0] and [self.taxi[0]+1,self.taxi[1]] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("baixo", self.mapa_dimensao,[self.taxi[0]+1, self.taxi[1]], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("baixo", self.mapa_dimensao,[self.taxi[0]+1, self.taxi[1]], self.obstaculos, [self.taxi[0]+1, self.taxi[1]], self.destino, self.carro_com_passageiro))


        if self.taxi[1] != 0 and [self.taxi[0],self.taxi[1]-1] not in self.obstaculos:
            if self.carro_com_passageiro == False:
                sucessors.append(Taxi("esquerda", self.mapa_dimensao,[self.taxi[0], self.taxi[1]-1], self.obstaculos, self.passageiro, self.destino, self.carro_com_passageiro))
            else:
                sucessors.append(Taxi("esquerda", self.mapa_dimensao,[self.taxi[0], self.taxi[1]-1], self.obstaculos, [self.taxi[0], self.taxi[1]-1], self.destino, self.carro_com_passageiro))

        if self.taxi[1] != self.mapa_dimensao[1] and [self.taxi[0],self.taxi[1]+1] not in self.obstaculos:
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


    def show_path(self, op, mapa_dimensao, taxi, obstaculos, passageiro, destino):
        state = Taxi(self, op, mapa_dimensao, taxi, obstaculos, passageiro, destino)
        algorithm = AEstrela()
        result = algorithm.search(state)
        if result != None:
            return result.show_path()
        else:
            return 'Nao tem solucao'
    
    def env(self):
        return self.operator + str(self.taxi) + str(self.carro_com_passageiro)
    
    def cost(self):
        if "passageiro" in self.operator:
            return 5
        else:
            return 1

def main():
    state = Taxi("", [7,5], [0,0], [[0,3],[1,3],[2,3]], [0,5], [4,0])
    algorithm = AEstrela()
    result = algorithm.search(state, trace=True)
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    return result

if __name__ == '__main__':
    main()