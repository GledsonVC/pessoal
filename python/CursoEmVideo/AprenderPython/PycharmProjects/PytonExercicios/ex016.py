# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n = float(input('Digite um número Real: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))
# print sem importar função alguma
print('o valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))
