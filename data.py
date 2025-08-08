from random import randint
from random import choice
d100 = randint(1, 100)
d20 = randint(1, 20)
d12 = randint(1, 12)
d10 = randint(1, 10)
d8 = randint(1, 8)
d6 = randint(1, 6)
d4 = randint(1, 4)

class Item:
    def __init__(self, name, description, tipo, value, usable):
        self._name = name
        self._description = description
        self._tipo = tipo
        self._value = value
        self.equipped = False
        self.usable = usable
    
    def __str__(self):
        return self._name

class Arma(Item):
    def __init__(self, name, description, tipo, value, usable, equipped, damage):
        super().__init__(name, description, tipo, value, usable)
        self._equipped = equipped
        self._damage = damage
    
    def __str__(self):
        return self._name

faca = Arma('faca', 'uma faca de serra', 'corpo-a-corpo', 10, False, False, randint(1, 4))

class Inimigo:
    def __init__(self, name, hp, arma):
        self._name = name
        self._hp = hp
        self._equipado = [arma]
        self._inventory = ['poção']
    
    def __str__(self):
        return self._name
    
    def inventario(self):
        lista = []
        for item in self._inventory:
            if hasattr(item, '_name'): lista.append(item._name)
            else: lista.append(item)
        return lista
monstro = Inimigo('monstro', 12, faca)

class Player:
    def __init__(self):
        self.win = False
        self._name =  ''
        self._hp = 12
        self._equipado = ['']
        self._armas = [faca]
        self.xposition = ''
        self.yposition = ''
        self._inventory = ['mapa', 'poção', 'pé de cabra']

    def __str__(self):
        return self._name
    
    def inventario_armas(self):
        lista = []
        for arma in self._armas: lista.append(arma._name)
        return lista
    
    def inventario(self):
        lista = []
        for item in self._inventory:
            if hasattr(item, '_name'): lista.append(item._name)
            else: lista.append(item)
        return lista

player1 = Player()
player1.xposition = 2
player1.yposition = 5



#MAPA (TILES, ITENS E FUNÇÃO)

a = ' ' #neblina --limitando a movimentação
b = '▢' #parede --limitando a movimentação

#mapa0 --floresta neblinosa
w = '=' #estrada
x = '^' #floresta
y = '▨' #armazém
z = '⛶' #casa abandonada

#mapa1 --dentro da casa
r = ' ' #representa o caminho andável pelo personagem
s = '#' #representa um lugar bloqueado por entulhos (fazer função para retirar)
p = ']' #porta fechada
d = '[' #porta aberta

#mapa de itens
c = 'chave'
i = 'item'

def gerar_mapa(numero):
    match numero:
        case 0:
            mapa_geral = [[a, a, a, a, a, a, a],
                          [a, z, p, z, x, x, a],
                          [a, x, w, w, w, w, a],
                          [a, x, w, x, x, x, a],
                          [a, x, w, x, y, x, a],
                          [a, x, w, x, x, x, a],
                          [a, a, a, a, a, a, a]]

            mapa_base =  [[a, a, a, a, a, a, a],
                          [a, z, p, z, x, x, a],
                          [a, x, w, w, w, w, a],
                          [a, x, w, x, x, x, a],
                          [a, x, w, x, y, x, a],
                          [a, x, w, x, x, x, a],
                          [a, a, a, a, a, a, a]]
            
            mapa_items = [[a, a, a, a, a, a, a],
                          [a, a, a, a, a, a, a],
                          [a, i, a, a, a, i, a],
                          [a, a, a, a, a, a, a],
                          [a, a, a, a, c, a, a],
                          [a, a, i, a, a, a, a],
                          [a, a, a, a, a, a, a]]

            mapa_atual = 0
            return mapa_geral, mapa_base, mapa_atual, 2, 5, mapa_items
        case 1:
            mapa_geral = [[b, b, b, b, b, b, b],
                          [b, b, r, b, r, b, b],
                          [b, b, s, b, r, b, b],
                          [b, p, r, r, r, r, b],
                          [b, b, r, b, s, b, b],
                          [b, b, r, b, r, b, b],
                          [b, b, b, b, b, b, b]]
            
            mapa_base =  [[b, b, b, b, b, b, b],
                          [b, b, r, b, r, b, b],
                          [b, b, s, b, r, b, b],
                          [b, p, r, r, r, r, b],
                          [b, b, r, b, s, b, b],
                          [b, b, r, b, r, b, b],
                          [b, b, b, b, b, b, b]]

            mapa_items = [[a, a, a, a, a, a, a],
                          [a, a, c, a, i, a, a],
                          [a, a, a, a, a, a, a],
                          [a, a, a, a, a, a, a],
                          [a, a, a, a, a, a, a],
                          [a, a, i, a, i, a, a],
                          [a, a, a, a, a, a, a]]

            mapa_atual = 1
            return mapa_geral, mapa_base, mapa_atual, 1, 3, mapa_items

#INFORMAÇÕES DE LUGARES DO MAPA

FLORESTA = {
    'DESCRICAO': 'A floresta é densa e sombria. Ela é perfurada por uma névoa fina. A lama do chão dificulta um pouco seu movimento.',
    'INFO': 'Algo não está certo. A neblina é quente e não houve chuva alguma. Algo esta errado.',
    'ITEM_USAVEL': None
}

ESTRADA = {
    'DESCRICAO': 'A estrada de barro se estende ao largo, o barro molhado impregna em suas botas.',
    'INFO': 'Pegadas recém formadas no barro levam para a casa abandonada.',
    'ITEM_USAVEL': None
}

ARMAZEM = {
    'DESCRICAO': 'Um armazém velho de madeira caindo aos pedaços. Têm alguns caixotes no canto da sala.',
    'ITEM_USAVEL': None
}

CASA = {
    'DESCRICAO': 'Uma casa abandonada caindo aos pedaços. As venezianas estão quebradas e o teto parece parcialmente no lugar.',
    'INFO': '~~~.'
}

DESCRICAO_DO_INTERIOR_DA_CASA = {
    1: 'A parede da casa está tomada de mofo e outros tipos de fungos.',
    2: 'O chão e a parede estão estranhamente úmidos',
    3: 'O chão está repleto de cacos de vidros das janelas.',
    4: 'Uma parte do teto desabou, mas não atrapalha a passagem.',
    5: 'Uma névoa fina se faz visível no interior da casa.',
    6: 'A vegetação cresce pelas arestas do piso.'
}

ESPACO = {
    'INFO': 'Pegadas de barro são visíveis no chão.',
    'ITEM_USAVEL': None
}

ENTULHOS = {
    'DESCRICAO': '',
    'INFO': '',
    'ITEM_USAVEL': 'pé de cabra'
}

PORTA = {
    'DESCRICAO': 'A porta está um pouco velha, mas ainda segue em pé.',
    'INFO': 'A porta está trancada.',
    'ITEM_USAVEL': 'chave',
    'PORTA_FECHADA': True
}

CHAVE = {
    'ITEM': 'chave'
}

#lista_itens = [pocao, flecha, esmeralda]

#ITEM = {
#    'ITEM': lista_itens[d4-1]
#}
