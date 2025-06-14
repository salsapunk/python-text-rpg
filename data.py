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
    def __init__(self, name, description, tipo, value, damage):
        super().__init__(name, description, tipo, value)
        self.equipped = False
        self._damage = damage
    
    def __str__(self):
        return self._name

espada_longa = Arma('Espada longa', 'Uma espada com uma lâmina grande e afiada', 'Corpo-a-copro', '50', d8)
espada_longa.equipped = True
arco = Arma('Arco', 'Um arco', 'Distância', '50', d6)

class Player:
    def __init__(self):
        self.win = False
        self._name =  ''
        self._level = 1
        self._hp = 12
        self._equipado = [espada_longa]
        self._armas = [arco]
        self._xposition = j
        self._yposition = i
        self._inventory = ['Escudo', 'Mapa']
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

a = ' ' #limitando a movimentação
w = '=' #estrada
x = '^' #floresta
y = '▨' #armazém
z = '⛶' #casa abandonada

def gerar_mapa0():
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
    mapa_base = [[a, a, a, a, a, a, a, a, a, a, a, a, a],
                  [a, z, z, z, z, z, z, z, x, x, x, x, a],
                  [a, z, z, z, z, z, z, z, x, x, x, x, a],
                  [a, x, w, w, w, w, w, w, x, x, x, x, a],
                  [a, x, w, x, x, x, x, w, w, w, x, x, a],
                  [a, x, w, x, x, x, x, x, x, w, x, x, a],
                  [a, x, w, x, y, y, y, x ,x, w, x, x, a],
                  [a, x, w, x, y, y, y, x, x, w, x, x, a],
                  [a, x, w, x, x, x, x, x, x, w, x, x, a],
                  [a, a, a, a, a, a, a, a, a, a, a, a, a]]
    return mapa_geral, mapa_base

#i = 8 #(de 0 a 13)
#j = 2 #(de 0 a 10)
#player inicia na posição mapa[8][2]

FLORESTA = {
    'DESCRICAO': 'A floresta é densa e sombria. Ela é perfurada por uma névoa fina. A lama do chão dificulta um pouco seu movimento.',
    'INFO': 'Algo não está certo. A neblina é quente e não houve chuva alguma. Algo esta errado.',
    'ITEM': None
}

ESTRADA = {
    'DESCRICAO': 'A estrada de barro se estende ao largo, o barro molhado impregna em suas botas.',
    'INFO': 'Pegadas recém formadas no barro levam para a casa abandonada.',
    'ITEM': 'espada'
}

ARMAZEM = {
    'DESCRICAO': 'Um armazém velho de madeira caindo aos pedaços. Têm alguns caixotes no canto da sala.',
    'INFO': 'Dentro dos caixotes tem uma chave que parece de uma casa.',
    'ITEM': 'chave média'
}

CASA = {
    'DESCRICAO': 'Uma casa abandonada caindo aos pedaços. As venezianas estão quebradas o teto parcialmente no lugar.',
    'INFO': 'A porta está trancada. Sua fechadura tem um formato de *chave média*.',
    'ITEM': None
}
