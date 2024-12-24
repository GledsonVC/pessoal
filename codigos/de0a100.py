from random import randint
from time import sleep
e = int(input('Digite um nº bem grande: '))
print(f'Pensei em um n  de 0 a {e}')
sleep(3)
print('Será q tu consegue advinhar?')
p = randint(0, e)
n = int(input('Qual nº pensei? '))
j = 0
while p != n:
    sleep(1)
    print('-='*33)
    print('Humm')
    if n < p:
        print('É pouco! Cabra dapeste.')
    else:
        print('É muito! cabra macho')
    j += 1
    n = int(input('Tenti outro n° rapa: '))
sleep(2)
j += 1
print(f'\nACERTO MIZERAAAVI!!! \nEm {j} jogada')