# matriz = [[i+j for j in range(3)] for i in range(1, 10, 3)]

# print(matriz)

# print(matriz[1][0])
from data import *
from game import *

def posicao():
    print(player1._position)
    #print(para esquerda tem blablabla, ...)
    prompt_posicao = input('Para qual direção gostaria de ir?')
    direcoes = ['oeste', 'leste', 'norte', 'sul']
    match prompt_posicao in direcoes:
        case 'oeste':
            player1._xposition += 1
            print(mapa[player1._xposition][player1._yposition])
        case 'leste':
            player1._xposition -= 1
            print(mapa[player1._xposition][player1._yposition])
        case 'norte':
            player1._yposition += 1
            print(mapa[player1._xposition][player1._yposition])
        case 'sul':
            player1._yposition -= 1
            print(mapa[player1._xposition][player1._yposition])

posicao()