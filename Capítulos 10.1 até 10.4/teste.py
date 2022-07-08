#Exercício 10.8 Crie uma nova conta, agora tendo João e José como clientes e saldo
#igual a 500.

from bancos import Banco
from clientes import Cliente
from contas import Conta

joao = Cliente('João da Silva', '3241-5599')
maria = Cliente('Maria da Silva', '7231-9955')
jose = Cliente('José Vargas', '9721-3040')
contaJM = Conta([joao, maria], 100)
contaJ = Conta([jose], 10)
tatu = Banco('Tatú')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()