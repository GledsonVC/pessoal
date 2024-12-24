# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
# uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
n = int(input('Quantos termo vc quer mostrar? '))
n1 = 0
n2 = 1
n3 = 1
while n != 0:
    print('{} -> '.format(n1), end='')
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    n -= 1
print('Fim')

