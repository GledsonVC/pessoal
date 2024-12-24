# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# OBS:exercício 061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.
# OBS exercício 051:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
mais = 1
pa = p
cont = 10
t = 10
while mais != 0:
    while (cont > 0 ):
        print('{} -> '.format(p), end='')
        p = p + r
        cont -= 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais? '))
    cont = mais
    t += mais
print('Progressão finalizada com {} termos mostrado'.format(t))
