#Exercício 9.12 Modifique o programa do Exercício 9.11 para também registrar a
#linha e a coluna de cada ocorrência da palavra no arquivo. Para isso, utilize listas
#nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.


ocorrências = {}
with open('Wiki.txt', 'rt') as entrada:
    linhas = entrada.readlines()
    numero_linha = 0
    for linha in linhas:
        numero_linha += 1
        coluna = 0
        for palavra in linha.split():
            coluna += 1
            if palavra not in ocorrências:
                ocorrências[palavra] = {}
                ocorrências[palavra]['Numero de Ocorrencias'] = 1
                ocorrências[palavra]['Linhas de Ocorrencias'] = []
                ocorrências[palavra]['Colunas de Ocorrencias'] = []
                ocorrências[palavra]['Linhas de Ocorrencias'].append(numero_linha)
                ocorrências[palavra]['Colunas de Ocorrencias'].append(coluna)

            else:
                ocorrências[palavra]['Numero de Ocorrencias'] += 1
                ocorrências[palavra]['Linhas de Ocorrencias'].append(numero_linha)
                ocorrências[palavra]['Colunas de Ocorrencias'].append(coluna)

print(ocorrências)