# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
pesado = leve = 0
while True:
    cadastro = list()
    cadastro.append(str(input('Nome: ').strip().upper()))
    cadastro.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = cadastro[1]
    else:
        if cadastro[1] > pesado:
            pesado = cadastro[1]
        if cadastro[1] < leve:
            leve = cadastro[1]
    pessoas.append(cadastro[:])
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
    cadastro.clear()
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesado:.2f}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == pesado:
        print(f'[{c[0]}] ', end='')
print()
print(f'O menor peso foi de {leve:.2f}Kg. Peso de:', end='')
for c in pessoas:
    if c[1] == leve:
        print(f'[{c[0]}] ', end='')
print()
