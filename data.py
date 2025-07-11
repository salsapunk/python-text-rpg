from random import randint
d100 = randint(1, 100)
d20 = randint(1, 20)
d12 = randint(1, 12)
d10 = randint(1, 10)
d8 = randint(1, 8)
d6 = randint(1, 6)
d4 = randint(1, 4)


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
        self.usable = ''
    
    def __str__(self):
        return self._name

class Arma(Item):
    def __init__(self, name, description, tipo, value, equipped, damage):
        super().__init__(name, description, tipo, value)
        self._equipped = equipped
        self._damage = damage
    
    def __str__(self):
        return self._name

espada_longa = Arma('Espada longa', 'Uma espada com uma lâmina grande e afiada', 'Corpo-a-copro', 15, True, d8)
arco = Arma('Arco', 'Um arco', 'Distância', 10, False, d6)
flecha = Item('Flecha', 'Flecha para o arco', 'Consumível', 5)
flecha.usable = True
pocao = Item('Poção', 'Poção que restaura vida.', 'Consumível', 20)
pocao.usable = True
esmeralda = Item('Esmeralda', 'Uma esmeralda valiosa.', 'Vendível', 250)


class Player:
    def __init__(self):
        self.win = False
        self._name =  ''
        self._level = 1
        self._hp = 12
        self._equipado = [espada_longa]
        self._armas = [arco]
        self.xposition = ''
        self.yposition = ''
        self._inventory = ['escudo', 'mapa', 'chave']
        self._experience = 0
        self._skills = {
            "Força": '1',
            "Agilidade": '1',
            "Inteligência": '1',
            "Carisma": '1'
        }

    def __str__(self):
        return self._name
    
    def inventario_armas(self):
        lista = []
        for arma in self._armas:
            lista.append(arma._name)
        return lista

player1 = Player()
player1.xposition = 2
player1.yposition = 5

#geral
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
p = ']' #porta para o mapa1

#mapa de itens
c = 'chave'
i = 'item'

def gerar_mapa(numero):
    match numero:
        case 0:
            mapa_geral = [[a, a, a, a, a, a, a],
                          [a, z, z, z, x, x, a],
                          [a, x, w, w, w, w, a],
                          [a, x, w, x, x, x, a],
                          [a, x, w, x, y, x, a],
                          [a, x, w, x, x, x, a],
                          [a, a, a, a, a, a, a]]

            mapa_base =  [[a, a, a, a, a, a, a],
                          [a, z, z, z, x, x, a],
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

FLORESTA = {
    'DESCRICAO': 'A floresta é densa e sombria. Ela é perfurada por uma névoa fina. A lama do chão dificulta um pouco seu movimento.',
    'INFO': 'Algo não está certo. A neblina é quente e não houve chuva alguma. Algo esta errado.',
}

ESTRADA = {
    'DESCRICAO': 'A estrada de barro se estende ao largo, o barro molhado impregna em suas botas.',
    'INFO': 'Pegadas recém formadas no barro levam para a casa abandonada.',
}

ARMAZEM = {
    'DESCRICAO': 'Um armazém velho de madeira caindo aos pedaços. Têm alguns caixotes no canto da sala.',
    'INFO': 'Dentro dos caixotes tem uma chave que parece de uma casa.',
}

CASA = {
    'DESCRICAO': 'Uma casa abandonada caindo aos pedaços. As venezianas estão quebradas o teto parcialmente no lugar.',
    'INFO': 'A porta está trancada. Sua fechadura tem um formato de uma *chave média*.',
    'ITEM_USAVEL': 'chave',
    'PORTA_FECHADA': True
}

ESPACO = {
    'ITEM_USAVEL': 'l'
}

CHAVE = {
    'ITEM': 'chave'
}

lista_itens = [pocao, pocao, flecha, flecha, flecha, esmeralda]

ITEM = {
    'ITEM': lista_itens[d6-1]
}
