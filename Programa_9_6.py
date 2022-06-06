#Exercício 9.17 Altere o Programa 9.6 para exibir o tamanho da agenda no menu
#principal.

#Exercício 9.19 Altere a função lista para que exiba também a posição de cada
#elemento.

#Exercício 9.20 Adicione a opção de ordenar a lista por nome no menu principal.

#Exercício 9.21 Nas funções de alterar e apaga , peça que o usuário confirme a alteração
#e exclusão do nome antes de realizar a operação em si.

#Exercício 9.22 Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi gravada.
#Você pode usar uma variável para controlar quando a lista foi alterada (novo,
#altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.

#Exercício 9.23 Altere o programa para ler a última agenda lida ou gravada ao inicializar.
#Dica: utilize outro arquivo para armazenar o nome.

# Programa 9.6 - Controle de uma agenda de telefones
agenda = []
status = 'Salvo'
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
    global status
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    status = 'Não salvo'
def apaga():
    global agenda
    global status
    nome = pede_nome()
    p = pesquisa(nome)
    confirmar = input('Tem certeza que quer excluir o contato?(S/N)').upper()
    if p is not None and confirmar == 'S':
        del agenda[p]
    else:
        print('Nome não encontrado.')
    status = 'Não salvo'
def altera():
    global status
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado:')
        mostra_dados(nome, telefone)
        confirmar = input('Tem certeza que quer alterar o contato? (S/N)').upper()
        if confirmar == 'S':
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado.')
    status = 'Não salvo'
def lista():
    print('\nAgenda\n\n------')
    for i, e in enumerate(agenda):
        print(i)
        mostra_dados(e[0], e[1])
    print('------\n')
def lê():
    global agenda
    global status
    global arquivo_ultimo
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])
    status = 'Salvo'
    arquivo_ultimo = nome_arquivo
def grava():
    global status
    global arquivo_ultimo
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')
    status = 'Salvo'
    arquivo_ultimo = nome_arquivo
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')
def ordenar():
    global agenda
    agenda = sorted(agenda, key= lambda agenda: agenda[0])
def menu():
    print(f"""
    Status da lista atual: {status}
    Tamanho atual da agenda: {len(agenda)}

    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Ordenar Agenda
    
    0 - Sai
    """)
    return valida_faixa_inteiro('Escolha uma opção ', 0, 7)
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
    elif opção == 7:
        ordenar()


