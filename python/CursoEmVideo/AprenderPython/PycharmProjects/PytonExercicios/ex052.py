# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[32m{}'.format(c), end=' ')
        cont += 1
    else:
        print('\33[31m{}'.format(c), end=' ')
print('\33[m')
if(cont == 2):
    print('O numero {} foi divisível {} vezes'.format(n, cont))
    print('E por isso ele É PRIMO!')
else:
    print('O numero {} foi divisível {} vezes'.format(n, cont))
    print('E por isso ele NÃO É PRIMO!')
