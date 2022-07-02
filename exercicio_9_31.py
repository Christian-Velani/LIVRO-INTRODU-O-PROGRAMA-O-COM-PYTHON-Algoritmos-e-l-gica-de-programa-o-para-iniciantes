# Exercício 9.31 Crie um programa que corrija o Programa 0.0 de forma a verificar se z existe e é um diretório.

import os.path
if os.path.exists('z'):
    print('z existe')
    if os.path.isdir('z'):
        print('z é um diretório')
    else:
        print('z não é um diretório')
else:
    print('z não existe')