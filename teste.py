import os
import os.path
import time
import sys
nome = sys.argv[1]
print(f"NoMe: {nome}")
print(f"TaManho: {os.path.getsize(nome)} ")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")
print(f"Modiflcado: {time.ctime(os.path.getmtime(nome))} ")
print(f"Acessado: {time.ctime(os.path.getatime(nome))}")