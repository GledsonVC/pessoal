# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.
# OBS exercício 051:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
print('Gerador de PA')
print('-='*10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
pa = p
c = 1
while c != 11:
    print('{}'.format(pa), end='')
    print(' -> ', end='')
    pa = pa + r
    c += 1
print('FIM')
