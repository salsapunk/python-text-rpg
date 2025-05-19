class Player:
    def __init__(self):
        self._name =  ''
        self._level = 1
        self._lives = 1
        self._items = []
        self._position = (0, 0)
        self._inventory = {}
        self._experience = 0
        self._skills = {
            "Força": '1',
            "Agilidade": '1',
            "Inteligência": '1',
            "Carisma": '1'
        }
player1 = Player()

w = '𐦂' #estrada
x = '𖠰' #floresta
y = '▨' #templo da floresta
z = '⛶' #casa abandonada

mapa = [[z, z, z, z, z, z, z, x, x, x, x],
        [z, z, z, z, z, z, z, x, x, x, x],
        [x, w, w, w, w, w, w, x, x, x, x],
        [x, w, x, x, x, x, w, w, w, x, x],
        [x, w, x, x, x, x, x, x, w, x, x],
        [x, w, x, y, y, y, x ,x, w, x, x],
        [x, w, x, y, y, y, x, x, w, x, x],
        [x, w, x, x, x, x, x, x, w, x, x]]

print('Mapa:')
for tile in mapa:
    resultado = ' '.join(tile)
    print(resultado)
    
DESCRICAO = 'descrição'
INFO = 'info'
SIDE_UP = 'foward'
SIDE_DOWN = 'down', 'back'
SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'

FLORESTA = {
    'DESCRICAO': None,
    'INFO': None,
}