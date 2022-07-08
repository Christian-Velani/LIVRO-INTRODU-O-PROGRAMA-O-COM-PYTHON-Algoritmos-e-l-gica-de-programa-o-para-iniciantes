# Programa 10.1 - Conta com registro de operações e extrato

#Exercício 10.6 - Altere o programa de forma que a mensagem saldo insuficiente
#seja exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível

#Exercicio 10.7 - Modifique o método resumo da classe Conta para exibir
#o nome eo telefone de cada cliente
from pydoc import cli


class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        for i in self.clientes:
            print(f'Nome: {i.nome} Telefone: {i.telefone}') #Este código não funciona para contas com apenas 1 cliente
        print(f"CC Número: {self.numero} Saldo: {self.saldo: 10.2f}\n")
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print('Saldo Insuficiente')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])
    def extrato(self):
        print(f'Extrato CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n  Saldo: {self.saldo:10.2f}\n')

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])