'''

'''

from data import *
import os
from time import sleep
import platform
import sys

system = platform.system()
match system:
    case 'Linux': os_var = 'clear'
    case 'Windows': os_var = 'cls'

#os.system(os_var)

def title_screen():
    os.system(os_var)
    print('#' * 29)
    print(f'[ Bem-vindo ao RPG de texto ]')
    print('#' * 29)
    print('   [ Feito por Salsapunk ]')
    print('      .:    Jogar    :.')
    print('      .:    Ajuda    :.')
    print('      .:    Sair     :.')
    title_screen_options()

def title_screen_options():
    option = input('> ')
    if option.lower() == 'jogar': setup_game()
    elif option.lower() == 'ajuda': pass
    elif option.lower() == 'sair': sys.exit()
    else:
        print('Comando inválido, tente novamente.')
        sleep(1)
        title_screen()

def prompt():
    print('O que deseja fazer? (andar, olhar, investigar, usar, pegar, mapa, personagem, equipar, sair)')
    prompt = input('> ').lower()
    if prompt not in ['olhar', 'investigar', 'usar', 'pegar', 'andar', 'mapa', 'sair', 'personagem', 'equipar']: print('Digite um comando válido!')
    else:
        match prompt:
            case 'olhar': info('DESCRICAO')
            case 'investigar': info('INFO')
            case 'usar':
                item = input('Qual item gostaria de usar?\n> ')
                usar(player1, item)
            case 'pegar': pegar()
            case 'andar': posicao()
            case 'personagem': menu_personagem()
            case 'equipar':
                item = input('Qual arma gostaria de equipar?\n> ')
                equipar(item)
            case 'mapa': mostrar_mapa()
            case 'sair': sys.exit()

def definir_mapa(numero):
    global mapa, mapa_mostrar, mapa_atual, mapa_itens
    mapa, mapa_mostrar, mapa_atual, mapa_itens = gerar_mapa(numero)

posicaox = player1.xposition
posicaoy = player1.yposition

def desequipar(equipado, inventario):
    item_velho = equipado[0]
    inventario.append(item_velho)
    equipado.remove(item_velho)

def equipar(arma):
    inventario = player1._armas
    equipado = player1._equipado
    i = 0
    if arma == 'vazio':
        desequipar(equipado, inventario)
        equipado.append('')
        print('O item foi desequipado.')
    else:
        while i < len(inventario):
            arma_inventario = inventario[i]._name.lower()
            arma.lower()
            if arma == arma_inventario:
                equipavel = inventario[i]
                if equipado[0] == '':
                    equipado.remove('')
                else:
                    equipado[0]._equipped = False
                    desequipar(equipado, inventario)
                equipado.append(equipavel)
                inventario.remove(equipavel)
                print('O item foi equipado.')
            i = i+1        

def arma_equipada():
    if player1._equipado[0] =='': return 'vazio'
    else: return player1._equipado[0]._name

def menu_personagem():
    armas = player1.inventario_armas()
    inventario = player1.inventario()
    print('-' * 29)
    print('Menu do personagem')
    print(f'Nome: {player1._name}')
    print(f'Vida: {player1._hp}')
    print(f'Arma equipada: {arma_equipada()}')
    print(f'Armas no inventário: {' ,'.join(armas)}')
    print(f'Invetário: {', '.join(inventario)}')
    print('-' * 29)

def atualizar_posicao_player():
    global posicao_player, posicao_player_itens
    posicao_player = mapa_mostrar[player1.yposition][player1.xposition]
    posicao_player_itens = mapa_itens[player1.yposition][player1.xposition]
    if checar_posicao(posicao_player) == 'porta': mudar_mapa()

def checar_posicao_alem(tile):
    if mapa[player1.yposition+1][player1.xposition] == tile: 
        return True
    elif mapa[player1.yposition-1][player1.xposition] == tile: 
        return True
    elif mapa[player1.yposition][player1.xposition+1] == tile:
        return True
    elif mapa[player1.yposition][player1.xposition-1] == tile: 
        return True
    else: 
        return False

def checar_1_maior(tile):
    x = 0
    y = 0
    if mapa[player1.yposition+1][player1.xposition] == tile: 
        x = player1.xposition
        y = player1.yposition + 1
    elif mapa[player1.yposition-1][player1.xposition] == tile:
        x = player1.xposition
        y = player1.yposition - 1
    elif mapa[player1.yposition][player1.xposition+1] == tile:
        x = player1.xposition + 1
        y = player1.yposition
    elif mapa[player1.yposition][player1.xposition-1] == tile:
        x = player1.xposition - 1
        y = player1.yposition
    else: None
    return x, y

def usar(alvo, item):
    inventario = alvo.inventario()
    if item not in inventario: 
        if alvo == player1: print('Você não possui esse item!')
        return
    if item == 'chave' or item == 'pé de cabra':
        print(f'Você usou {item}')
        match item:
            case 'chave':
                if checar_posicao_alem(']'):
                    x, y = checar_1_maior(']')
                    mapa[y][x] = '['
                    mapa_mostrar[x][y] = '['
                    alvo._inventory.remove(item)
                    destrancando_portas(lugar)
            case 'pé de cabra':
                if checar_posicao_alem('#'):
                    x, y = checar_1_maior('#')
                    mapa[y][x] = ' '
                    mapa_mostrar[y][x] = ' '
                    print('Você retirou os escombros e agora a passagem está livre.')
                else: print('Não há lugar para usar o pé de cabra.')
    else:
        match item:
            case 'poção':
                vida_recuperada = randint(1, 8)
                alvo._hp += vida_recuperada
        alvo._inventory.remove(item)

def destrancando_portas(lugar):
    match lugar:
            case PORTA:
                if PORTA['PORTA_FECHADA']:
                    PORTA['PORTA_FECHADA'] = False
                    print('Você destrancou a porta.')
                    mudar_mapa()
                else: print('A porta já está aberta.')

def info(funcao):
    lugar = puxar_data()
    if posicao_player_itens == 'chave' or posicao_player_itens == 'item':
        if funcao == 'INFO': mensagem_tesouro()
        else:
            print(lugar[funcao])
    elif lugar == ESPACO and funcao == 'DESCRICAO': print(choice(list(DESCRICAO_DO_INTERIOR_DA_CASA.values())))
    else:
        print(lugar[funcao])

def mensagem_tesouro():
    match posicao_player_itens:
        case 'chave': print('Algo está brilhando no chão, parece uma chave.')
        case 'item': print('Tem algo no chão. Pegue para saber o que é.')

def checar_posicao(posicao_player):
    match mapa_atual:
        case 0:
            if posicao_player == ' ': return 'neblina'
            elif posicao_player == '=': return 'estrada'
            elif posicao_player == '^': return 'floresta'
            elif posicao_player == '▨': return 'armazem'
            elif posicao_player == '⛶': return 'casa'
            elif posicao_player == ']': return 'porta_fechada'
            elif posicao_player == '[': return 'porta_aberta'
        case 1:
            if posicao_player == ' ': return 'espaço'
            elif posicao_player == '#': return 'escombros'
            elif posicao_player == '▢': return 'parede'
            elif posicao_player == ']': return 'porta_fechada'
            elif posicao_player == '[': return 'porta_aberta'

def mudar_mapa():
    if PORTA['PORTA_FECHADA'] == False:
        quer_entrar = input('Você gostaria de entrar?\n> ').lower()
        while quer_entrar not in ['sim', 'não', 's', 'nao', 'n']: print('Responda com Sim ou Não!')
        if quer_entrar in ['sim', 's']: escolher_mapa()
        else: print('Você olha assustado para a casa e decide voltar...')
    else: None

definir_mapa(0)
atualizar_posicao_player()

#melhorar código
def pegar():
    posicao_player_itens = mapa_itens[player1.yposition][player1.xposition]
    if posicao_player_itens == 'chave':
        player1._inventory.append('chave')
        posicao_player_itens = ' '
        print('Você pegou uma chave.')
    elif posicao_player_itens == 'item':
        item = ITEM['ITEM']
        player1._inventory.append(item._name.lower())
        posicao_player_itens = ' '
        print(f'Você pegou {item}.')
    else: print('Não há nenhum item aqui!')

def mostrar_mapa():
    mapa[player1.yposition][player1.xposition] = 'o'
    for tile in mapa:
        resultado = ' '.join(tile)
        print(resultado)
    legenda()

def puxar_data():
    tile = checar_posicao(posicao_player)
    match tile:
        case 'floresta': return FLORESTA
        case 'armazem': return ARMAZEM
        case 'casa': return CASA
        case 'estrada': return ESTRADA
        case 'espaço': return ESPACO
        case 'entulhos': return ENTULHOS
        case 'porta': return PORTA
        case 'porta_fechada': return PORTA

def pode_andar():
    match checar_posicao(mapa[player1.yposition][player1.xposition]):
        case 'estrada': return 'sim'
        case 'floresta': return 'sim'
        case 'armazem': return 'sim'
        case 'casa': return 'sim'
        case 'neblina':
            print('A neblina está muito densa para esse lado, é melhor não se afastar...')
            sleep(2)
            return 'não'
        case 'espaço': return 'sim'
        case 'escombros':
            print('Escombros impedem o caminho. Ache um jeito de desbloquear a passagem!')
            sleep(2)
            return 'não'
        case 'parede':
            print('Por mais que a casa esteja abandonada e caindo aos pedaços, a parede ainda é sólida.')
            sleep(2)
            return 'não'
        case 'porta_aberta': return 'sim'
        case 'porta_fechada': return 'não'

def escolher_mapa(): 
    match mapa_atual:
        case 0:
            numero = 1
        case 1:
            numero = 0
    definir_mapa(numero)

def legenda():
    print(posicao_player_itens)
    match mapa_atual:
        case 0:
            print("'=' representa a estrada")
            print("'^' representa a floresta")
            print("'▨' representa um armazém")
            print("'⛶' representa uma casa abandonada")
            print("'o' representa onde seu personagem está")
        case 1:
            print("'#' representa os escombros que bloqueiam o caminho")
            print("'▢' representa as paredes da casa")
            print("' ' representa o espaço da casa, explore e investigue para ver se acha algo!")
            print("'o' representa onde seu personagem está")

def mudar_tile(tile, yposition_antiga, xposition_antiga):
    match tile:
        case 'floresta': mapa[yposition_antiga][xposition_antiga] = '^'
        case 'estrada': mapa[yposition_antiga][xposition_antiga] = '='
        case 'armazem': mapa[yposition_antiga][xposition_antiga] = '▨'
        case 'casa': mapa[yposition_antiga][xposition_antiga] = '⛶'
        case 'espaço': mapa[yposition_antiga][xposition_antiga] = ' '
        case 'porta': mapa[yposition_antiga][xposition_antiga] = ']'
    mapa[player1.yposition][player1.xposition] = 'o'
    atualizar_posicao_player()

def posicao():
    while True:
        print('Para qual direção gostaria de ir?')
        print('(Ou use "sair" para sair)')
        prompt_posicao = input('> ').lower()
        direcoes = ['oeste', 'leste', 'norte', 'sul', 'sair', 'mapa']
        if prompt_posicao not in direcoes: print('Essa direção não existe. Tente novamente!')
        elif prompt_posicao == 'sair': break
        else:
            if mapa_atual == 0: mapa[posicaoy][posicaox] = '='
            else: mapa[posicaoy][posicaox] = ' '
            xposition_antiga = player1.xposition
            yposition_antiga = player1.yposition
            match prompt_posicao:
                case 'oeste': player1.xposition -= 1
                case 'leste': player1.xposition += 1
                case 'norte': player1.yposition -= 1
                case 'sul': player1.yposition += 1
            chave = pode_andar()
            tile = checar_posicao(mapa_mostrar[yposition_antiga][xposition_antiga])
            if chave == 'sim':
                mudar_tile(tile, yposition_antiga, xposition_antiga)
                break
            else:
                player1.xposition = xposition_antiga
                player1.yposition = yposition_antiga

def gerar_inimigo():
    global inimigo
    inimigo = monstro
    inimigo._hp = 12
    print(f'Um {monstro._name} aparece em sua frente!')
    return True

def acao_inimigo():
    if inimigo._hp <= 6 and inimigo._inventory[0] == 'poção': 
        usar(inimigo, 'poção')
        print("O inimigo usa uma poção!")
    else: 
        ataque(inimigo, player1)
        print("O inimigo te ataca!")

def prompt_combate(em_combate):
    while em_combate and player1._hp > 0:
        print(inimigo._hp)
        print('O que deseja fazer? (atacar, usar, equipar, personagem, fugir, sair)')
        prompt_combate = input('> ').lower()
        if prompt_combate not in ['atacar', 'defender', 'usar', 'equipar', 'personagem', 'fugir', 'sair']: print('Digite um comando válido!')
        else:
            match prompt_combate:
                case 'atacar': em_combate = ataque(player1, inimigo);
                case 'usar': 
                    item = input('Qual item gostaria de usar?\n> ')
                    usar(player1, item)
                case 'equipar': 
                    item = input('Qual arma gostaria de equipar?\n> ')
                    equipar(item)
                case 'personagem': 
                    menu_personagem()
                    continue
                case 'fugir': 
                    em_combate = fugir()
                    continue
                case 'sair': sys.exit()
            if em_combate == False: break
            acao_inimigo()

def ataque(atacante, alvo):
    if atacante._equipado[0] == '': dano = randint(1, 2)
    else: dano = atacante._equipado[0]._damage
    alvo._hp -= dano
    if alvo._hp <= 0:
        print(f'{alvo._name} morreu')
        return False
    else: return True

def fugir():
    inimigo = None
    return False

def setup_game():
    os.system(os_var)
    # print('Qual o nome do seu personagem? \n')
    # player1._name = input('> ')
    while player1._hp > 0 and player1.win == False:
        prompt()
        #prompt_combate(gerar_inimigo())
    if player1._hp == 0: print("Game Over. Você morreu.")
    else: print('Parabéns! Você venceu o jogo!')


title_screen()
