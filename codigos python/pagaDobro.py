print('\n Programa cada dia sendo pago o dobro iniciando por R$0,01')
dias = int(input('Digite a quantidade de dias: '))
valorTotal =  0.00
dobra = 0.01

"""Solução com For"""
for dia in range(dias):
    valorTotal += dobra
    dobra *= 2
print(f'\nEm {dias} dias recebeu o valor  de R${valorTotal}')

"""Com while"""
valorTotal =  0.00
dobra = 0.01
contador = 0
while contador < dias:
    valorTotal += dobra
    dobra *= 2
    contador += 1
print(f'\nEm {dias} dias recebeu o valor  de R${valorTotal}')

"""Sem loop"""
valorTotal =  0
dobra = 0.01
valorTotal = dobra * ((2**dias) - 1) / (2 - 1)
print(f'\nEm {dias} dias recebeu o valor  de R${valorTotal}')