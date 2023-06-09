from TaxiDriver import Taxi
from datetime import datetime

def test_simples():  
    inicio = datetime.now()
    state = Taxi("", [5,7], [0,0], [[0,3],[1,3],[2,3]], [0,5], [4,0])
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.g == 30

def test_passageiro_dentro():  
    inicio = datetime.now()
    state = Taxi("", [5,7], [3,5], [[0,3],[1,3],[2,3]], [3,5], [4,0], True)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.g == 11

def test_dificil1():  
    inicio = datetime.now()
    state = Taxi("", [5,7], [0,0], [[0,3],[1,3],[2,3],[2,4],[2,5],[3,1],[4,1]], [0,4], [4,0])
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.g == 38

def test_dificil2():  
    inicio = datetime.now()
    state = Taxi("", [8,4], [1,2], [[7,1],[6,1],[5,1],[4,1],[3,1],[2,3],[1,3], [0,3]], [7,0], [7,2])
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.g == 30

def test_dificil3():  
    inicio = datetime.now()
    state = Taxi("", [8,8], [6,0], [[8,1],[7,1],[6,1],[5,1],[4,1],[3,1],[2,3],[1,3],[0,3],[8,5],[7,5],[6,5],[5,5],[4,5],[3,5],[2,7],[1,7],[0,7]], [7,4], [7,6])
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.g == 35

def test_impossivel():
    inicio = datetime.now()
    state = Taxi("", [2,2], [0,0], [[0,1],[1,0]], [1,1], [0,0])
    r = state.show_path()
    fim = datetime.now()
    print(fim-inicio)
    assert r == 'Nao achou solucao'
