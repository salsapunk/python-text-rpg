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
    case 'Linux':
        os_var = 'clear'
    case 'Windows':
        os_var = 'cls'

#os.system(os_var)

def pre_main():
    player1._xposition = 2
    player1._yposition = 8

mapa0, mapa0_mostar = gerar_mapa0()
posicao_player = mapa0_mostar[player1._yposition][player1._xposition]

def title_screen():
    pre_main()
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
    if option.lower() == 'jogar':
        setup_game()
    elif option.lower() == 'ajuda':
        pass
        #help()
    elif option.lower() == 'sair':
        sys.exit()
    else:
        print('Comando inválido, tente novamente.')
        sleep(1)
        title_screen()

def mostrar_mapa():
    mapa0[player1._yposition][player1._xposition] = 'o'
    for tile in mapa0:
        resultado = ' '.join(tile)
        print(resultado)

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
    print('O que deseja fazer? (andar, olhar, investigar, usar, pegar, personagem, equipar, sair)')
    prompt = input('> ').lower()
    if prompt not in ['olhar', 'investigar', 'usar', 'pegar', 'andar', 'sair', 'personagem', 'equipar']:
        print('Digite um comando válido!')
    else:
        match prompt:
            case 'olhar':
                info('DESCRICAO')
            case 'investigar':
                info('INFO')
            case 'usar':
                pass
            case 'pegar':
                item = input('Qual item você quer pegar?\n >')
                pegar(item)
                pass
            case 'inspecionar':
                pass
            case 'andar':
                posicao()
            case 'personagem':
                menu_personagem()
            case 'equipar':
                item = input('Qual arma gostaria de equipar?')
                equipar(item)
            case 'sair':
                sys.exit()

#NÃO FUNCIONA
# def equipar(arma):
#     lista = player1._armas
#     print('debug1')
#     i = 0
#     len(lista) == x
#     for a in x:
#         arma_inventario = lista[i]._name
#         if arma == arma_inventario:
#             print('debug2')
#             inventario = player1._armas
#             equipado = player1._equipado
#             if  lista[i].equipped == True:
#                 print('debug3')
#                 lista[i].equipped = False
#                 item_velho = equipado[0]
#                 inventario.append(item_velho)
#                 equipado.remove(item_velho)
#             print('debug4')
#             equipado.append(arma)
#             inventario.remove(arma)
#             print('O item foi equipado!')
#         i = i+1


def pegar(item):
    lugar = puxar_data()
    #NÃO FUNCIONA
    if item == lugar['ITEM']:
        player1._inventory.append(item)
        lugar['ITEM'] = 'None'

def mostrar_skills():
    for atributos in player1._skills:
        for value in player1._skills[atributos]:
            if atributos == 'Carisma':
                print(f'{atributos}: {''.join(value)}.')
            else:
                print(f'{atributos}: {''.join(value)};')

def menu_personagem():
    armas = []
    lista = player1._armas
    i = 0
    while i < len(lista):
        arma = str(lista[i]._name)
        armas.append(arma)
        i = i + 1
    
    print('-' * 29)
    print('Menu do personagem')
    print(f'Nome: {player1._name}')
    print(f'Level: {player1._level}')
    print(f'Vida: {player1._hp}')
    print(f'Experiência: {player1._experience}')
    print(f'Arma equipada: {player1._equipado[0]._name}')
    print(f'Armas não equipadas: {' ,'.join(armas)}')
    print(f'Invetário: {', '.join(player1._inventory)}')
    mostrar_skills()
    print('-' * 29)
    

def usar():
    item = input('Qual item gostaria de usar?\n >')
    if item not in player1._inventory:
        print('Você não possui esse item!')
    else:
        print(f'Você usou {item}')

def info(funcao):
    lugar = puxar_data()
    print(lugar[funcao])
    
def puxar_data():
    tile = checar_posicao(posicao_player)
    match tile:
        case 'floresta':
            return FLORESTA
        case 'armazem':
            return ARMAZEM
        case 'casa':
            return CASA
        case 'estrada':
            return ESTRADA

def atributos_settings():
    while True:
        os.system(os_var)
        print('Distribua três pontos entre os seguintes atributos, que já começam com 1 \n')
        atributos()
        print(player1._skills)
        print('Tem certeza da distribuição dos atributos?')
        r = input('[Sim / Não] \n' '> ').lower()
        if r in ['nao', 'não', 'n']:
            print('Tente novamente')
        elif r in ['sim', 's']:
            os.system(os_var)
            break
        else:
            print('Responda com Sim ou Não. Faça novamente!')
            sleep(2)

def checar_posicao(posicao_player):
    if posicao_player == ' ':
        return 'neblina'
    elif posicao_player == '=':
        return 'estrada'
    elif posicao_player == '^':
        return 'floresta'
    elif posicao_player == '▨':
        return 'armazem'
    elif posicao_player == '⛶':
        return 'casa'

def pode_andar():
    #DEBUG print(checar_posicao(mapa0[player1._yposition][player1._xposition]))
    match checar_posicao(mapa0[player1._yposition][player1._xposition]):
        case 'estrada':
            return 'sim'
        case 'floresta':
            return 'sim'
        case 'armazem':
            return 'sim'
        case 'casa':
            quer_entrar = input('Você gostaria de entrar na casa? (Sim/Não)').lower()
            while quer_entrar not in ['sim', 'não', 's', 'nao', 'n']:
                print('Responda com Sim ou Não!')
                return
            if quer_entrar in ['sim', 's']:
                return 'sim'
            else: 
                mensagem_nao_casa = 'Você olha assustado para a casa e decide voltar...'
                for caractere in mensagem_nao_casa:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    
                return 'não'
        case 'neblina':
            mensagem_posicao_limite = 'A neblina está muito densa para esse lado, é melhor não se afastar...'
            for caractere in mensagem_posicao_limite:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                sleep(0.05)
            match player1._xposition:
                case 12:
                    player1._xposition = 11
                case 0:
                    player1._xposition = 1
            match player1._yposition:
                case 9:
                    player1._yposition = 8
                case 0:
                    player1._yposition = 1
            return 'não'

def legenda():
    print("'=' representa a estrada")
    print("'^' representa a floresta")
    print("'▨' representa um armazem")
    print("'⛶' representa uma casa abandonada")
    print("'o' representa onde seu personagem está")

def posicao():
    while True:
        print('Para qual direção gostaria de ir?')
        print('(Ou escreva "Sair" para sair, ou "Mapa" para ver o mapa e as legendas)')
        prompt_posicao = input('> ').lower()
        direcoes = ['oeste', 'leste', 'norte', 'sul', 'sair', 'mapa']
        if prompt_posicao not in direcoes:
            print('Essa direção não existe. Tente novamente!')
        elif prompt_posicao == 'sair':
            sys.exit()
        elif prompt_posicao == 'mapa':
            mostrar_mapa()
            legenda()
        else:
            mapa0[8][2] = '='
            xposition_antiga = player1._xposition
            yposition_antiga = player1._yposition
            match prompt_posicao:
                case 'oeste':
                    player1._xposition -= 1
                case 'leste':
                    player1._xposition += 1
                case 'norte':
                    player1._yposition -= 1
                case 'sul':
                    player1._yposition += 1
            chave = pode_andar()
            tile = checar_posicao(mapa0_mostar[yposition_antiga][xposition_antiga])
            if chave == 'sim':
                match tile:
                    case 'floresta':
                        mapa0[yposition_antiga][xposition_antiga] = '^'
                    case 'estrada':
                         mapa0[yposition_antiga][xposition_antiga] = '='
                    case 'armazem':
                         mapa0[yposition_antiga][xposition_antiga] = '▨'
                    case 'casa':
                         mapa0[yposition_antiga][xposition_antiga] = '⛶'
                mapa0[player1._yposition][player1._xposition] = 'o'
                break
            else:
                player1._xposition = xposition_antiga
                player1._yposition = yposition_antiga


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