#Exercício 9.11 Crie um programa que leia um arquivo e crie um dicionário em que
#cada chave é uma palavra e cada valor é o número de ocorrências no arquivo.

ocorrências = {}
with open('Wiki.txt', 'rt') as entrada:
    linhas = entrada.readlines()
    for linha in linhas:
        for palavra in linha.split():
            if palavra not in ocorrências:
                ocorrências[palavra] = 1
            else:
                ocorrências[palavra] += 1

print(ocorrências)