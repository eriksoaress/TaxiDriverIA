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



Quais as operações sobre os estados? (detalhe como cada operação irá alterar os estados e quais as condições para cada operação ser executada)
As operações possíveis são "cima", "direita", "baixo", "esquerda" que movimentam o taxi alterando os valores da sua coordenada de acordo com a operação. Também há as operações "pegar passageiro" que altera o valor de "carro_com_passageiro" para True e a "deixar passageiro" altera o valor de "carro_com_passageiro" para False



Que algoritmo de busca foi utilizado para resolver este problema considerando que a solução apresentada precisa ser ótima e que deve ser processada na ordem de segundos, no máximo em poucos minutos?


A equipe fez uso de heurísticas? Se sim, explique as heurísticas utilizadas.


Quais são os limites da solução? A solução consegue tratar mapas com que dimensões? Quão complexo pode ser a estrutura de obstáculos?


Uma explicação de como deve ser usada a implementação com exemplos.