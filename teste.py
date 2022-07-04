from clientes import Cliente
from contas import Conta
joao = Cliente( "João da Silva ", "777-1234 ")
Maria = Cliente( "Maria da Silva ", "555-4321")

conta = Conta((joao, Maria), '11113101812101010', 1500)
conta.resumo()
conta.saque(1000)
conta.resumo()
conta.saque(50)
conta.resumo()
conta.deposito(200)
conta.resumo()