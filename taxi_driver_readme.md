# TaxiDriverIA
*Integrantes:*\
Erik Leonardo Soares de Oliveira\
Gustavo Antony de Assis\
Matheus Aguiar de Jesus


O que é relevante representar nos estados do mundo? Como os estados são estruturados (estrutura de dados) e qual o significado dela (dos campos)?
- É relevante representar a dimensão do mapa que será utilizado ["quantidade linhas", "quantidade colunas"]

- local do taxi que é estruturado na forma de uma lista ["linha", "coluna"];

- local do passageiro que é estruturado na forma de uma lista ["linha", "coluna"];

- coordenadas do destino final que é estruturado na forma de uma lista ["linha", "coluna"];

- locais dos obstáculos que é estrurado na forma de uma lista de listas [["linha_obst1","coluna_obst1"], ["linha_obst2","coluna_obst2"], ["linha_obst3","coluna_obst3"]]



Mostre como ficam representados os estados inicial e final segundo a representação adotada.

\
-Estado inicial:
- taxi: [0,0]
- passageiro: [0,5]
- destino: [4,0]
- obstáculos: [[0,3],[1,3],[2,3]]
- dimensao: [5,7]

-Estado final:
- taxi: [4,0]
- passageiro: [4,0]
- destino: [4,0]
- obstáculos: [[0,3],[1,3],[2,3]]
- dimensao: [5,7]



Quais as operações sobre os estados? (detalhe como cada operação irá alterar os estados e quais as condições para cada operação ser executada)\
\
Operações:\
- "cima" - move o taxi uma linha para cima no mapa. (EXEMPLO taxi:[1,1] -> taxi:[0,1])

- "baixo" - move o taxi uma linha para baixo no mapa. (EXEMPLO taxi:[1,1] -> taxi:[2,1])

- "esquerda" - move o taxi uma coluna para a esquerda no mapa. (EXEMPLO taxi:[1,1] -> taxi:[1,0])

- "direita" - move o taxi uma coluna para a direita no mapa. (EXEMPLO taxi:[1,1] -> taxi:[1,2])

- "pegar passageiro" - altera o valor do parâmetro "carro_com_passageiro" para True. (EXEMPLO carro_com_passageiro: False -> carro_com_passageiro: True)

- "deixar passageiro" - altera o valor do parâmetro "carro_com_passageiro" para False. (EXEMPLO carro_com_passageiro: True -> carro_com_passageiro: False)



Que algoritmo de busca foi utilizado para resolver este problema considerando que a solução apresentada precisa ser ótima e que deve ser processada na ordem de segundos, no máximo em poucos minutos?
- Foi utilizado o algoritmo de busca A*, haja vista que precisava considerar o custo das operações para que ele seja ótimo e também gostaríamos de utilizar heurísticas a fim de tornar a execução do algoritmo mais rápida.


A equipe fez uso de heurísticas? Se sim, explique as heurísticas utilizadas.
Sim, a heurística utilizada foi distância de Manhattan entre o taxi e o passageiro, e após pegar o passageiro foi calculada a distância de Manhattan entre o taxi e o destino final. Foi utilizada essa heurística porque ela simula a distância entre o ponto atual e o de destino e também considerando a forma com que o taxi se movimenta (vertical e horizontal).

Quais são os limites da solução? A solução consegue tratar mapas com que dimensões? Quão complexo pode ser a estrutura de obstáculos?



Uma explicação de como deve ser usada a implementação com exemplos.
