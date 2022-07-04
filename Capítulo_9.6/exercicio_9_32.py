#Exercício 9.32 Modifique o Programa 9.9 de forma a receber o nome do arquivo ou
#diretório a verificar pela linha de comando. Imprima se existir e se for um arquivo
#ou um diretório.

import os.path
import sys
if os.path.exists(sys.argv[1]):
    print(f'{sys.argv[1]} existe')
    if os.path.isdir(f'{sys.argv[1]}'):
        print(f'{sys.argv[1]} é um diretório')
    elif os.path.isfile(sys.argv[1]):
        print(f'{sys.argv[1]} é um arquivo')
else:
    print(f'{sys.argv[1]} não existe')