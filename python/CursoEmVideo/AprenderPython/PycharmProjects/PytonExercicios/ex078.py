# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c}: ')))
print(f'Voce digitou os valores {lista}')
print(f'O maior valor foi {max(lista)} nas posições ', end='')
for c in range(0, len(lista)):
    if max(lista) == lista[c]:
        print(f'{c}... ', end='')
print(f'\nO menor valor foi {min(lista)} nas posições ', end='')
for c in range(0, len(lista)):
    if min(lista) == lista[c]:
        print(f'{c}... ', end='')