from random import randint
d100 = randint(1, 100)
d20 = randint(1, 20)
d12 = randint(1, 12)
d10 = randint(1, 10)
d8 = randint(1, 8)
d6 = randint(1, 6)
d4 = randint(1, 4)

i = 8
j = 2

class Player:
    def __init__(self):
        self._name =  ''
        self._level = 1
        self._hp = 12
        self._arma = []
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
    
    def __str__(self):
        return self._name

player1 = Player()

class Inimigo:
    def __init__(self, name, level, hp, arma, skills):
        self._name = name
        self._level = level
        self._hp = hp
        self._arma = arma
        self._skills = {
            "Força": skills[0],
            "Agilidade": skills[1],
            "Inteligência": skills[2],
            "Carisma": skills[3]
        }
    
    def __str__(self):
        return self._name
        
class Item:
    def __init__(self, name, description, tipo, value):
        self._name = name
        self._description = description
        self._tipo = tipo
        self._value = value
        self.equipped = False
        self.usable = False
    
    def __str__(self):
        return self._name

class Arma(Item):
    def __init__(self):
        super().__init__(name, description, tipo, value)
        self.equipped = False
    
    def __str__(self):
        return self._name

a = ' ' #limitando a movimentação
w = '=' #estrada
x = '^' #floresta
y = '▨' #armazém
z = '⛶' #casa abandonada

mapa_geral = [[a, a, a, a, a, a, a, a, a, a, a, a, a],
              [a, z, z, z, z, z, z, z, x, x, x, x, a],
              [a, z, z, z, z, z, z, z, x, x, x, x, a],
              [a, x, w, w, w, w, w, w, x, x, x, x, a],
              [a, x, w, x, x, x, x, w, w, w, x, x, a],
              [a, x, w, x, x, x, x, x, x, w, x, x, a],
              [a, x, w, x, y, y, y, x ,x, w, x, x, a],
              [a, x, w, x, y, y, y, x, x, w, x, x, a],
              [a, x, w, x, x, x, x, x, x, w, x, x, a],
              [a, a, a, a, a, a, a, a, a, a, a, a, a]]

posicao_player = mapa_geral[player1._yposition][player1._xposition]

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