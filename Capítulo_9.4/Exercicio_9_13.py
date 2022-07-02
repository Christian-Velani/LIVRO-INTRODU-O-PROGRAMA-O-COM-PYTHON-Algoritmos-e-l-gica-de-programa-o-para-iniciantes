#Exercício 9.13 Crie um programa que imprima as linhas de um arquivo. Esse programa
#deve receber três parâmetros pela linha de comando: o nome do arquivo, a
#linha inicial e a última linha a imprimir.

import sys

with open(sys.argv[1], 'r') as entrada:
    linhas = entrada.readlines()
    try:
        for linha in range(int(sys.argv[2]), int(sys.argv[3])):
            print(linhas[linha])
    except IndexError():
        print('Número de inicio ou fim incorreto!')