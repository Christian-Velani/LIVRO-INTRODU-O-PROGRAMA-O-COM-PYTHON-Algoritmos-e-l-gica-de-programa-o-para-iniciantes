#Exercício 9.15 Altere o Programa 7.2, o jogo da forca. Utilize um arquivo em que
#uma palavra seja gravada a cada linha. Use um editor de textos para gerar o arquivo.
#Ao iniciar o programa, utilize esse arquivo para carregar (ler) a lista de palavras.
#Experimente também perguntar o nome do jogador e gerar um arquivo com o
#número de acertos dos cinco melhores.

import random
with open('Palavras.txt', 'rt') as entrada, open('Scores.txt', 'wt') as saida:
    jogar = 1
    palavras = entrada.readlines()
    jogadores = []
    acertos_jogadores = []
    while jogar != 0:
        palavra = random.choice(palavras).lower().strip()
        jogador = input('Digite o nome de quem vai tentar adivinhar: ')
        digitadas = []
        acertos = []
        erros = 0
        if jogador.upper() not in jogadores:
            jogadores.append(jogador.upper())
            acertos_jogadores.append(0)   
        while True:
            senha = ''
            for letra in palavra:
                senha += letra if letra in acertos else '.'
            print(senha)
            if senha == palavra:
                print('Você acertou!')
                acertos_jogadores[jogadores.index(jogador.upper())] += 1
                break
            tentativa = input('\nDigite uma letra:').lower().strip()
            if tentativa in digitadas:
                print('Você já tentou esta letra')
                continue
            else:
                digitadas += tentativa
                if tentativa in palavra:
                    acertos += tentativa
                else:
                    erros += 1
                    print('Você errou!')
            print('X==:--\nX : ')
            print('X  O ' if erros >= 1 else 'X')
            linha2 = ''
            if erros == 2:
                linha2 = '  | '
            elif erros == 3:
                linha2 = ' \| '
            elif erros >= 4:
                linha2 = ' \|/'
            print(f'X{linha2}')
            linha3 = ''
            if erros == 5:
                linha3 += ' /'
            elif erros >= 6:
                linha3 += ' / \ '
            print(f'X{linha3}')
            print('X\n===========')
            if erros == 7:
                print('Enforcado!')
                break
        jogar = int(input('Para parar de jogar digite 0: '))
        melhores = []
    for alocador in range(5):
        alocar = {'Nome':'', 'Pontos': 0}
        maior_ponto = 0
        for pontos in acertos_jogadores:
            if maior_ponto < pontos and jogadores[acertos_jogadores.index(pontos)] not in melhores:
                nome = jogadores[acertos_jogadores.index(pontos)]
                maior_ponto = pontos
            else:
                continue
        alocar['Nome'] = nome
        alocar['Pontos'] = maior_ponto
        saida.write(f'Jogador: {alocar["Nome"]}')
        saida.write('\n')
        saida.write(f'Pontos: {alocar["Pontos"]}')
        saida.write('\n')
        melhores.append(nome)
