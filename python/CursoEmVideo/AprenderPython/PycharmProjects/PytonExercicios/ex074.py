# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(0, 9),
         randint(0, 9),
         randint(0, 9),
         randint(0, 9),
         randint(0, 9))
print(f'Os valores sorteados foram: {tupla}')
print(f'O menor valor foi: {sorted(tupla)[0]}')
print(f'O maior valor foi : {sorted(tupla)[-1]}')

# PROFESSOR FEZ COM FUNÇÃO MAX() E MIN() QUE NÃO CONHECIA OS DOIS ULTIMOS e o primeiro print fez com for
print('Os valores sorteados foram: ', end='')
for c in tupla:
    print(f'{c} ', end='')
print(f'\nO menor valor foi: {min(tupla)}')
print(f'O maior valor foi : {max(tupla)}')
