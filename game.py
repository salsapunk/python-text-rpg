'''

'''

from data import *
import os
from random import randint
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
    if option.lower() == 'jogar':
        setup_game()
    elif option.lower() == 'ajuda':
        pass
        #help()
    elif option.lower() == 'sair':
        sys.exit()
    while option.lower not in ['jogar', 'ajuda', 'sair']:
        print('Comando inválido, tente novamente.')
        sleep(2)
        title_screen()

quitgame = 'quit'

def mostrar_mapa():
    print('Mapa:')
    for tile in mapa:
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
    prompt = input('> ').lower()
    if prompt not in ['olhar', 'investigar', 'usar', 'pegar', 'inspecionar']:
        print('Digite um comando válido!')
    elif prompt == 'quitgame':
        sys.exit()
    else:
        match prompt:
            case 'olhar':
                pass
            case 'investigar':
                pass
            case 'usar':
                pass
            case 'pegar':
                pass
            case 'inspecionar':
                pass

def atributos_settings():
    os.system(os_var)
    q2 = 'Distribua três pontos entre os seguintes atributos, que já começam com 1 \n'
    for caractere in q2:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        sleep(0.05)
    atributos()
    print(player1._skills)
    print('Tem certeza da distribuição dos atributos?')
    r = input('[Sim / Não] \n' '> ').lower()
    if r in ['nao', 'não', 'n']:
        atributos_settings()
    if r in ['sim', 's']:
        pass

def posicao():
    mostrar_mapa()
    print(player1._xposition, player1._yposition)
    #print(para esquerda tem blablabla, ...)
    prompt_posicao = input('Para qual direção gostaria de ir? >').lower()
    direcoes = ['oeste', 'leste', 'norte', 'sul']
    if prompt_posicao not in direcoes:
        print('erro')
    else:
        match prompt_posicao:
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



def setup_game():
    os.system(os_var)
    q1 = 'Qual o nome do seu personagem? \n'
    for caractere in q1:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        sleep(0.05)
    name = input('> ')
    player1._name = name

    atributos_settings()
    print(f'Que o vento guie sua jornada, {player1._name}')
    sleep(0.5)
    posicao()


title_screen()