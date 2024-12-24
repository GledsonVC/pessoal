# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.
listaNum = [[], []]
for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    if numero%2 == 0:
        listaNum[0].append(numero)
    else:
        listaNum[1].append(numero)
listaNum[0].sort()
listaNum[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {listaNum[0]}')
print(f'Os valores ímpares digitados foram: {listaNum[1]}')
