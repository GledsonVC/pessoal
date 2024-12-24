# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
listaPar = []
listaImpar = []
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        listaPar.append(lista[c])
    else:
        listaImpar.append(lista[c])
print(f'Os valores digitados foram {lista}')
print(f'Lista de valores pares {listaPar}')
print(f'Lista de valores Ímpares {listaImpar}')