# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# obs: tentar fazer com comando while e for
n = int(input('Digite um valor para calcular seu fatorial: '))
f = n
if n == 0 or n == 1:
    print('Calculando {}! = 1'.format(n))
else:
    print('Calculando {}! = '.format(n), end='')
    while n != 1:
        if n == 2:
            print('{} x 1 = '.format(n), end='')
        else:
            print('{} x '.format(n), end='')
            f = f * (n-1)
        n -= 1
    print('{}'.format(f))
# com for para treinar
n = int(input('Digite um valor para calcular o fatorial: '))
f = n
if n == 0 or n == 1:
    print('Calculando {}! = 1'.format(n))
else:
    print('Calculando {}! = {} '.format(n, n), end='')
    for n in range(n, 1, -1):
        print('x {} '.format(n - 1), end='')
        f = f * (n-1)
    print('= {}'.format(f))
# com import math
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
# professor fez
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-=1
print('{}'.format(f))
