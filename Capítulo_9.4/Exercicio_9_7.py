#Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
#saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
#terá no máximo 60 linhas. Adicione na última linha de cada página o número da
#página atual e o nome do arquivo original.

LARGURA = 76
COMPRIMENTO = 60
numero_linhas = 0
numero_pagina = 1
with open('Wiki.txt', 'r') as arquivoOriginal, open('Arquivo Paginado.txt', 'w') as arquivoPaginado:
  frase = ''
  linhas = arquivoOriginal.readlines()
  for linha in linhas:
    if len(linha) <= LARGURA:
      if numero_linhas == COMPRIMENTO - 1:
        arquivoPaginado.write((f'Wiki; {numero_pagina}'.center(LARGURA)))
        arquivoPaginado.write('\n')
        numero_pagina += 1
        numero_linhas = 0
        arquivoPaginado.write(linha)
        numero_linhas += 1
      else:
        arquivoPaginado.write(linha)
        numero_linhas += 1
    else:
      for palavra in linha.split():
        if len(frase) + len(palavra) + len(' ') <= LARGURA:
          frase += palavra + ' '
        elif len(frase) + len(palavra) + len(' ') > LARGURA:
          if numero_linhas == COMPRIMENTO - 1:
            arquivoPaginado.write((f'Wiki; {numero_pagina}'.center(LARGURA)))
            arquivoPaginado.write('\n')
            numero_pagina += 1
            numero_linhas = 0
            arquivoPaginado.write(frase)
            arquivoPaginado.write('\n')
            numero_linhas += 1
            frase = ''
            frase += palavra + ' '
          else:
            arquivoPaginado.write(frase)
            arquivoPaginado.write('\n')
            numero_linhas += 1
            frase = ''
            frase += palavra + ' '
      if numero_linhas == COMPRIMENTO - 1:
        arquivoPaginado.write((f'Wiki; {numero_pagina}'.center(LARGURA)))
        arquivoPaginado.write('\n')
        numero_pagina += 1
        numero_linhas = 0
        arquivoPaginado.write(frase)
        arquivoPaginado.write('\n')
        numero_linhas += 1
      else:
        arquivoPaginado.write(frase)
        arquivoPaginado.write('\n')
        numero_linhas += 1