#Exercício 9.23 Altere o programa para ler a última agenda lida ou gravada ao inicializar.
#Dica: utilize outro arquivo para armazenar o nome.

# Programa 9.6 - Controle de uma agenda de telefones
agenda = []
arquivo_ultimo = ''
def pede_nome():
    return input('Nome: ')
def pede_telefone():
    return input('Telefone: ')
def mostra_dados(nome, telefone):
    print(f'Nome: {nome} Telefone: {telefone}')
def pede_nome_arquivo():
    return input('Nome do arquivo: ')
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print('Nome não encontrado.')
def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado.')
def lista():
    print('\nAgenda\n\n------')
    for e in agenda:
        mostra_dados(e[0], e[1])
    print('------\n')
def lê():
    global agenda
    global arquivo_ultimo
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])
    arquivo_ultimo = nome_arquivo
def grava():
    global arquivo_ultimo
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')
    arquivo_ultimo = nome_arquivo
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')
def menu():
    print("""
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    
    0 - Sai
    """)
    return valida_faixa_inteiro('Escolha uma opção ', 0, 6)
while True:
    with open('Última.txt', 'r') as ultima:
        ultima_agenda = ultima.read()
    print(f'Última agenda vista: {ultima_agenda}')
    opção = menu()
    if opção == 0:
        with open('Última.txt', 'w') as escrever:
            escrever.write(arquivo_ultimo)
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()

