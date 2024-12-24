# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
saque = int(input('Qual o valor que será sacado? R$'))
cinquenta = vinte = dez = um = 0
while saque != 0:
    while True:
        if 50 <= saque:
            cinquenta += 1
            saque -= 50
        else:
            if cinquenta != 0:
                print(f'Total de {cinquenta} cedulas de R$50')
            break
    while True:
        if 20 <= saque:
            vinte += 1
            saque -= 20
        else:
            if vinte != 0:
                print(f'Total de {vinte} cedulas de R$20')
            break
    while True:
        if 10 <= saque:
            dez += 1
            saque -= 10
        else:
            if dez != 0:
                print(f'Total de {dez} cedulas de R$10')
            break
    while True:
        if 1 <= saque:
            um += 1
            saque -= 1
        else:
            if um != 0:
                print(f'Total de {um} cedulas de R$1')
            break
'''
# professor pensou e estou tentando simular
valor = int(input('Que valor você quer sacar? R$'))
ced = 50
totalCed = 0
while True:
    if valor >= ced:
        valor -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cedula de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if valor == 0:
            break

