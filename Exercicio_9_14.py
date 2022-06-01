#Exercício 9.14 Crie um programa que leia um arquivo-texto e elimine os espaços
#repetidos entre as palavras e no fim das linhas. O arquivo de saída também não
#deve ter mais de uma linha em branco repetida.

def tratar_arquivo():
    linha_branco = 0
    with open('a4.txt', 'rt') as entrada, open('Arquivo Limpo.txt', 'wt') as saida:
        linhas = entrada.readlines()
        for indexe in range(len(linhas)):
            if linha_branco == 0:
                if linhas[indexe] == '\n':
                    frase = linhas[indexe]
                    linha_branco = 1
                    saida.write(' '.join(frase))
                else:
                    linha = linhas[indexe]
                    frase = linha.split()
                    saida.write(' '.join(frase))
                    saida.write('\n')
            else:
                if linhas[indexe] != '\n':
                    linha = linhas[indexe]
                    frase = linha.split()
                    linha_branco = 0
                    saida.write(' '.join(frase))
                    saida.write('\n')

tratar_arquivo()
