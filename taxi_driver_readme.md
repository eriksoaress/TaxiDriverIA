# TaxiDriverIA
*Autores:*\
Erik Leonardo Soares de Oliveira\
Gustavo Antony de Assis\
Matheus Aguiar de Jesus


O que é relevante representar nos estados do mundo? Como os estados são estruturados (estrutura de dados) e qual o significado dela (dos campos)?
- É relevante representar a dimensão do mapa que será utilizado ["quantidade linhas", "quantidade colunas"]

- local do taxi que é estruturado na forma de uma lista ["linha", "coluna"];

- local do passageiro que é estruturado na forma de uma lista ["linha", "coluna"];

- coordenadas do destino final que é estruturado na forma de uma lista ["linha", "coluna"];

- locais dos obstáculos que é estrurado na forma de uma lista de listas [["linha_obst1","coluna_obst1"], ["linha_obst2","coluna_obst2"], ["linha_obst3","coluna_obst3"]]

- por fim, se o passageiro já está ou não dentro do taxi, representado por um valor booleano True ou False.


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
Operações:   
- "cima" - move o taxi uma linha para cima no mapa. (EXEMPLO taxi:[1,1] -> taxi:[0,1])

- "baixo" - move o taxi uma linha para baixo no mapa. (EXEMPLO taxi:[1,1] -> taxi:[2,1])

- "esquerda" - move o taxi uma coluna para a esquerda no mapa. (EXEMPLO taxi:[1,1] -> taxi:[1,0])

- "direita" - move o taxi uma coluna para a direita no mapa. (EXEMPLO taxi:[1,1] -> taxi:[1,2])

- "pegar passageiro" - altera o valor do parâmetro "carro_com_passageiro" para True. (EXEMPLO carro_com_passageiro: False -> carro_com_passageiro: True)

- "deixar passageiro" - altera o valor do parâmetro "carro_com_passageiro" para False. (EXEMPLO carro_com_passageiro: True -> carro_com_passageiro: False)



Que algoritmo de busca foi utilizado para resolver este problema considerando que a solução apresentada precisa ser ótima e que deve ser processada na ordem de segundos, no máximo em poucos minutos?
- Foi utilizado o algoritmo de busca A*, haja vista que precisava considerar o custo das operações para que ele seja ótimo e também gostaríamos de utilizar heurísticas a fim de tornar a execução do algoritmo mais rápida.


A equipe fez uso de heurísticas? Se sim, explique as heurísticas utilizadas.
- Sim, a heurística utilizada foi distância de Manhattan entre o taxi e o passageiro, e após pegar o passageiro foi calculada a distância de Manhattan entre o taxi e o destino final. Foi utilizada essa heurística porque ela simula a distância entre o ponto atual e o de destino e também considerando a forma com que o taxi se movimenta (vertical e horizontal).


Quais são os limites da solução? A solução consegue tratar mapas com que dimensões? Quão complexo pode ser a estrutura de obstáculos?
- O tempo de execução do algoritmo pode variar para cada máquina que está executando, a depender de seu processador. Testamos a solução para mapas sem obstáculos e pegando o pior cenário possível (nesse caso o taxi e o destino estariam em um vértice do mapa enquanto que o passageiro estaria no vértice oposto), dessa forma executando para um mapa de dimensão 90 por 90 a execução ultrapassou o tempo de 5 minutos, demonstrando ser inviável para dimensões maiores que essa. Os obstáculos não foram considerados nesses testes pois eles não influenciam no desempenho, podendo então apresentar qualquer complexidade, o único impacto será em relação a ter ou não uma solução possível.
Teste: state = Taxi("", dimensao, [0,0], [], [0,89], [0,0])


Uma explicação de como deve ser usada a implementação com exemplos.
Para utilizar a implementação o usuário deve acessar o arquivo Testando.py e alterar o valor das variáveis da forma que tiver interesse, informando todas as informações relevantes, em seguida executar o arquivo para que seja exibido a solução encontrada.\
\
Exemplo:\
mapa_dimensao = [10,10]\
taxi = [0,0]\
obstaculos = [[2,2],[3,3]]\
passageiro = [5,5]\
destino = [6,9]\
carro_com_passageiro = False\
\
Também é possível utilizar uma interface mais amigável, através do arquivo TaxiGame. Ao executar tal arquivo será solicitado que você insira as dimensões do mapa que será utilizado. Após isso, uma janela será aberta para que você personalize o mapa da forma que quiser, selecionando o local dos obstáculos, do passageiro, destino, e do taxi clicando nos próprios quadrados do mapa (o limite para essa interface é 30 por 30).\
Cada um dos elementos da aplicação está representado por uma cor, segue a definição de cada uma abaixo:\
azul: obstáculos\
azul claro: passageiro\
amarelo: táxi\
roxo: destino\
rosa: destino + passageiro\
verde: táxi com passageiro