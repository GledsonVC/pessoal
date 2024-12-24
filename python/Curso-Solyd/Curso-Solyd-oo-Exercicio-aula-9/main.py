'''
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente posui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''
from clientes import Clientes
from conta import Conta

print('-='*20)
c1 = Clientes('Gledson Vasconcellos Cavalheiro', '306.150.128-25', 39)
'''print('nome:', cliente_sem_conta.nome,'\nCPF:', cliente_sem_conta.cfp,'\nIdade:', cliente_sem_conta.idade)'''
print(c1)

print('-='*20)
c1_com_conta = Conta(c1, 100, 10)

print('nome:', c1_com_conta.cliente.nome,'\nCPF:', c1_com_conta.cliente.cfp,'\nIdade:', c1_com_conta.cliente.idade)
print('Saldo:', c1_com_conta.saldo, '\nLimite:', c1_com_conta.limite)
c1_com_conta.saca(100.)
c1_com_conta.consulta_saldo()
c1_com_conta.saca(5)
c1_com_conta.consulta_saldo()
c1_com_conta.depositar(20.33)
c1_com_conta.consulta_saldo()
c1_com_conta.depositar(-3)
c1_com_conta.consulta_saldo()
