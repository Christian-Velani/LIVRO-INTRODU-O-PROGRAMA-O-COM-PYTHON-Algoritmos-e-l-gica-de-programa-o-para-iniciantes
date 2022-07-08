#Exercício 10.12 Observe o método saque das classes Conta e Contaespecial. Modifique
#o método saque da classe Conta de forma que a verificação da possibilidade
#de saque seja feita por um novo método, substituindo a condição atual. Esse novo
#método retornará verdadeiro se o saque puder ser efetuado, e falso, caso contrário.
#Modifique a classe ContaEspecial de forma a trabalhar com esse novo método.
#Verifique se você ainda precisa troca o método saque de ContaEspecial ou apenas 
#o novo método criado para verificar a possibilidade de saque.

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        for i in self.clientes:
            print(f'Nome: {i.nome} Telefone: {i.telefone}')
        print(f"CC Número: {self.numero} Saldo: {self.saldo: 10.2f}\n")
    def verificar_possivel_saque(self, valor):
        if valor <= self.saldo:
            return True
        else:
            return False
    def saque(self, valor):
        if self.verificar_possivel_saque(valor) == True:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print(f'Saldo Insuficiente para o saque de {valor}.')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])
    def extrato(self):
        print(f'Extrato CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n  Saldo: {self.saldo:10.2f}\n')
'''Devido a inserção do método de validação é possível, na ContaEspecial, só modificar esse metódo e não será necessário
a criação do metodo saque para a conta especial'''
class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite
    def verificar_possivel_saque(self, valor):
        if valor <= self.saldo + self.limite:
            return True
        else:
            return False
    def extrato(self):
        print(f'Extrato CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n Saldo: {self.saldo:10.2f}\n')
        print(f' Limite: {self.limite} ')
        print(f'\n Saldo Disponivél para saque: {self.limite - abs(self.saldo)}')