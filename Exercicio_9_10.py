#Exercício 9.10 Crie um programa que receba uma lista de nomes de arquivo e que
#gere apenas um grande arquivo de saída.

def criar_arquivo_grande(arquivos, final):
    with open(final, 'w') as arquivoFinal:
        for arquivo in arquivos:
            with open(arquivo, 'r') as entrada:
                arquivoFinal.write(entrada.read())
                arquivoFinal.write('\n')

lista_arquivos = ['a1.txt', 'a2.txt', 'a3.txt', 'Wiki.txt']

criar_arquivo_grande(lista_arquivos, 'Arquivo Grande.txt')