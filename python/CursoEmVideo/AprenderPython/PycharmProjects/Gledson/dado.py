from random import randint
from time import sleep
while True:
    while True:
        cont = str(input('Deseja jogar o dado? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if cont in 'N':
        break
    dado = randint(1, 6)
    print('-'*25)
    print(f'O resultado do dado foi:')
    sleep(1)
    print(f' \033[4m   \33[m')
    print(f'| {dado} |')
    print(f' ---')
    print('-'*25)
print('FIM...')
