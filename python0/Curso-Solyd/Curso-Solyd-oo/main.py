from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)
print('CAMINHÃO ROSA')
print('objeto: ', caminhao_rosa)
print('Tipo do objeto: ', type(caminhao_rosa))
print('Cor: ', caminhao_rosa.cor)
print('Rodas: ', caminhao_rosa.rodas)
print('Marca: ', caminhao_rosa.marca)
print('Tanque: ', caminhao_rosa.tanque)

print('')
carro_azul = Veiculo('azul', 4, 'bmw', 30)
print('CARRO AZUL')
print('Cor: ', carro_azul.cor)
print('Rodas: ', carro_azul.rodas)
print('Marca: ', carro_azul.marca)
print('Tanque: ', carro_azul.tanque)
print('Metodo posto de gasolina com o nome abastece')
carro_azul.abastecer(35)
print('Tanque: ', carro_azul.tanque)

print('')
carro_azul = Carro('azul', 'bmw', 30)
print('Cor: ', carro_azul.cor)
print('Rodas: ', carro_azul.rodas)
print('Marca: ', carro_azul.marca)
print('Tanque: ', carro_azul.tanque)
print('Metodo posto de gasolina com o nome abastece')
carro_azul.abastecer(35)
print('Tanque: ', carro_azul.tanque)


'''
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente posui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''
