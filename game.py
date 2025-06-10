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
        sleep(2)
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
    prompt = input('> ').lower()
    if prompt not in ['olhar', 'investigar', 'usar', 'pegar', 'andar']:
        print('Digite um comando válido!')
    elif prompt == 'sair':
        sys.exit()
    else:
        match prompt:
            case 'olhar':
                descricao(checar_posicao())
            case 'investigar':
                pass
            case 'usar':
                pass
            case 'pegar':
                pass
            case 'inspecionar':
                pass
            case 'andar':
                posicao()

def descricão():
    tile = checar_posicao()
    match tile:
        case 'floresta':
            None
        case 'estrada':
            None
        case 'casa':
            None
        case 'armazem':
            None

def atributos_settings():
    while True:
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
            print('Tente novamente')
        elif r in ['sim', 's']:
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
    print(checar_posicao(mapa0[player1._yposition][player1._xposition]))
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
    #os.system(os_var)
    #q1 = 'Qual o nome do seu personagem? \n'
    #for caractere in q1:
    #    sys.stdout.write(caractere)
    #    sys.stdout.flush()
    #    sleep(0.05)
    #name = input('> ')
    #player1._name = name

    #atributos_settings()
    #print(f'Que o vento guie sua jornada, {player1._name}')
    #sleep(0.5)
    while player1.win == False:
        prompt()
    print('Parabéns! Você venceu o jogo!')


title_screen()