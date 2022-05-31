#Exercício 9.9 Crie um programa que receba uma lista de nomes de arquivo e os
#imprima, um por um.

def imprimir_arquivos(lista):
    for arquivo in lista:
        with open(arquivo, 'r') as ler:
                print(ler.read())

lista = ['a1.txt', 'a2.txt', 'a3.txt', 'Wiki.txt']

imprimir_arquivos(lista)
        
