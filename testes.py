def pergunta():
    while True:
        p = input('Escreva uma pergunta a ser feita: ')
        r = input(f"Você confirma a pergunta '{p}'? [Sim/Não] \n > ").lower()
        if r in ['sim', 's']:
            print(f'Pergunta confirmada: {p}')
            break
        elif r in ['nao', 'não', 'n']:
            print('Pergunta rejeitada. Tente novamente.')
        else:
            print('Resposta inválida. Responda com Sim ou Não.')

pergunta()