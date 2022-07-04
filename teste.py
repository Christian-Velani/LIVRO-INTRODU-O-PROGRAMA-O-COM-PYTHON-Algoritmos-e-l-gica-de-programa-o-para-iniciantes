from clientes import Cliente
from contas import Conta
Joao = Cliente( "João da Silva ", "777-1234 ")
Maria = Cliente( "Maria da Silva ", "555-4321")

conta1 = Conta((Joao), 1, 1000)
conta2 = Conta([Maria, Joao], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()
conta1.saque(1500)