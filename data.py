i = 8
j = 2

class Player:
    def __init__(self):
        self._name =  ''
        self._level = 1
        self._lives = 1
        self._items = []
        self._xposition = j
        self._yposition = i
        self._inventory = {}
        self._experience = 0
        self._skills = {
            "Força": '1',
            "Agilidade": '1',
            "Inteligência": '1',
            "Carisma": '1'
        }
player1 = Player()

a = ' ' #limitando a movimentação
w = '=' #estrada
x = '^' #floresta
y = '▨' #templo da floresta
z = '⛶' #casa abandonada

mapa = [[a, a, a, a, a, a, a, a, a, a, a, a, a],
        [a, z, z, z, z, z, z, z, x, x, x, x, a],
        [a, z, z, z, z, z, z, z, x, x, x, x, a],
        [a, x, w, w, w, w, w, w, x, x, x, x, a],
        [a, x, w, x, x, x, x, w, w, w, x, x, a],
        [a, x, w, x, x, x, x, x, x, w, x, x, a],
        [a, x, w, x, y, y, y, x ,x, w, x, x, a],
        [a, x, w, x, y, y, y, x, x, w, x, x, a],
        [a, x, w, x, x, x, x, x, x, w, x, x, a],
        [a, a, a, a, a, a, a, a, a, a, a, a, a]]

#i = 8 #(de 0 a 13)
#j = 2 #(de 0 a 10)
#player inicia na posição mapa[8][2]

DESCRICAO = 'descrição'
INFO = 'info'
SIDE_UP = 'foward'
SIDE_DOWN = 'down', 'back'
SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'

#checar as posições nos 4 cantos cardeais pra ver qual o side up, down, left e right
FLORESTA = {
    'DESCRICAO': None,
    'INFO': None,
    'SIDE_UP': None,
}