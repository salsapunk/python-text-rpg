'''

'''

from data import *
import os
from time import sleep
import sys
import textwrap
import platform

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

def atributos():
    pontos = 3
    if pontos > 0:
        print(f'Pontos: {pontos}')
        print(f'Força: 1')
        forca = int(input('> '))
        if forca != 0: pontos = pontos - forca
        player1._skills['Força'] = 1 + forca
        
        print(f'Pontos: {pontos}')
        print(f'Agilidade: 1')
        agilidade = int(input('> '))
        if agilidade != 0: pontos = pontos - agilidade
        player1._skills['Agilidade'] = 1 + agilidade
        
        print(f'Pontos: {pontos}')
        print(f'Inteligência: 1')
        inteligencia = int(input('> '))
        if inteligencia != 0: pontos = pontos - inteligencia
        player1._skills['Inteligência'] = 1 + inteligencia
        
        print(f'Pontos: {pontos}')
        print(f'Carisma: 1')
        carisma = int(input('> '))
        if carisma != 0: pontos = pontos - carisma
        player1._skills['Carisma'] = 1 + carisma
        
        if pontos < 0: 
            print('Houve um erro na distribuição dos atributos, tente novamente.')
            atributos()

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
                usar(item)
            case 'pegar': pegar()
            case 'andar': posicao()
            case 'personagem': menu_personagem()
            case 'equipar':
                item = input('Qual arma gostaria de equipar?')
                equipar(item)
            case 'mapa': mostrar_mapa()
            case 'sair': sys.exit()

def equipar(arma):
    inventario = player1._armas
    equipado = player1._equipado
    i = 0
    while i < len(inventario):
        arma_inventario = inventario[i]._name.lower()
        arma.lower()
        if arma == arma_inventario:
            equipavel = inventario[i]
            if equipado[0]._equipped == True:
                equipado[0]._equipped = False
                item_velho = equipado[0]
                inventario.append(item_velho)
                equipado.remove(item_velho)
            equipado.append(equipavel)
            inventario.remove(equipavel)
            print('O item foi equipado!')
        i = i+1        

def mostrar_skills():
    for atributos in player1._skills:
        for value in player1._skills[atributos]:
            if atributos == 'Carisma':
                print(f'{atributos}: {''.join(value)}.')
            else:
                print(f'{atributos}: {''.join(value)};')

def menu_personagem():
    armas = player1.inventario_armas()
    inventario = player1.inventario()
    print('-' * 29)
    print('Menu do personagem')
    print(f'Nome: {player1._name}')
    print(f'Level: {player1._level}')
    print(f'Vida: {player1._hp}')
    print(f'Experiência: {player1._experience}')
    print(f'Arma equipada: {player1._equipado[0]._name}')
    print(f'Armas no inventário: {' ,'.join(armas)}')
    print(f'Invetário: {', '.join(inventario)}')
    mostrar_skills()
    print('-' * 29)

def usar(item):
    lugar = puxar_data()
    inventario = []
    for i in player1._inventory: inventario.append(i.lower())
    if item.lower() not in inventario: print('Você não possui esse item!')
    elif item.lower() != lugar['ITEM_USAVEL'].lower(): print('Você não pode usar esse item aqui.')
    else:
        print(f'Você usou {item}')
        player1._inventory.remove(item)
        match lugar:
            case CASA:
                CASA['PORTA_FECHADA'] = False
                print('Você destrancou a porta.')
                escolher_mapa()

def info(funcao):
    if posicao_player_itens == 'chave' or posicao_player_itens == 'item':
        if funcao == 'INFO': mensagem_tesouro()
        else:
            lugar = puxar_data()
            print(lugar[funcao])
    else:
        lugar = puxar_data()
        print(lugar[funcao])
    
def definir_mapa(numero):
    global mapa, mapa_mostrar, mapa_atual, posicaoy, posicaox, mapa_itens
    mapa, mapa_mostrar, mapa_atual, posicaoy, posicaox, mapa_itens = gerar_mapa(numero)
    player1.xposition = posicaoy
    player1.yposition = posicaox

def mensagem_tesouro():
    match posicao_player_itens:
        case 'chave': print('Algo está brilhando no chão, parece uma chave.')
        case 'item': print('Tem algo no chão. Pegue para saber o que é.')

def atualizar_posicao_player():
    global posicao_player, posicao_player_itens
    posicao_player = mapa_mostrar[player1.yposition][player1.xposition]
    posicao_player_itens = mapa_itens[player1.yposition][player1.xposition]

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
    print(player1._inventory)

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

def atributos_settings():
    while True:
        os.system(os_var)
        print('Distribua três pontos entre os seguintes atributos, que já começam com 1 \n')
        atributos()
        print(player1._skills)
        print('Tem certeza da distribuição dos atributos?')
        r = input('[Sim / Não] \n' '> ').lower()
        if r in ['nao', 'não', 'n']: print('Tente novamente')
        elif r in ['sim', 's']:
            os.system(os_var)
            break
        else:
            print('Responda com Sim ou Não. Faça novamente!')
            sleep(2)

def checar_posicao(posicao_player):
    match mapa_atual:
        case 0:
            if posicao_player == ' ': return 'neblina'
            elif posicao_player == '=': return 'estrada'
            elif posicao_player == '^': return 'floresta'
            elif posicao_player == '▨': return 'armazem'
            elif posicao_player == '⛶': return 'casa'
        case 1:
            if posicao_player == ' ': return 'espaço'
            elif posicao_player == '#': return 'escombros'
            elif posicao_player == '▢': return 'parede'

def pode_andar():
    match checar_posicao(mapa[player1.yposition][player1.xposition]):
        case 'estrada': return 'sim'
        case 'floresta': return 'sim'
        case 'armazem': return 'sim'
        case 'casa': return 'sim'
        case 'neblina':
            print('A neblina está muito densa para esse lado, é melhor não se afastar...')
            return 'não'
        case 'espaço':  return 'sim'
        case 'escombros':
            print('Escombros impedem o caminho. Ache um jeito de desbloquear a passagem!')
            return 'não'
        case 'parede':
            print('Por mais que a casa esteja abandonada e caindo aos pedaços, a parede ainda é sólida.')
            return 'não'

def mudar_mapa():
    lugar = puxar_data()
    if lugar['PORTA_FECHADA'] == False:
        quer_entrar = input('Você gostaria de entrar?\n>').lower()
        while quer_entrar not in ['sim', 'não', 's', 'nao', 'n']: print('Responda com Sim ou Não!')
        if quer_entrar in ['sim', 's']:
            match lugar:
                case CASA:
                    if mapa_atual == 0:
                        return 1
                    elif mapa_atual == 1:
                        return 0
        else: print('Você olha assustado para a casa e decide voltar...')
    else: return

def escolher_mapa(): mapa = definir_mapa(mudar_mapa())

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
                match tile:
                    case 'floresta': mapa[yposition_antiga][xposition_antiga] = '^'
                    case 'estrada': mapa[yposition_antiga][xposition_antiga] = '='
                    case 'armazem': mapa[yposition_antiga][xposition_antiga] = '▨'
                    case 'casa': mapa[yposition_antiga][xposition_antiga] = '⛶'
                    case 'espaço': mapa[yposition_antiga][xposition_antiga] = ' '
                mapa[player1.yposition][player1.xposition] = 'o'
                atualizar_posicao_player()
                break
            else:
                player1.xposition = xposition_antiga
                player1.yposition = yposition_antiga


def setup_game():
    os.system(os_var)
    # print('Qual o nome do seu personagem? \n')
    # name = input('> ')
    # player1._name = name
    # atributos_settings()
    # print(f'Que o vento guie sua jornada, {player1._name}')
    while player1.win == False:
        prompt()
    print('Parabéns! Você venceu o jogo!')


title_screen()