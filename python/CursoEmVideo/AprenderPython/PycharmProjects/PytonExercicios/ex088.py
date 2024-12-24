# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.
from random import randint
from time import sleep
print('-'*30)
print('{: ^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
listaDeJogos = list()
qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:=^30}'.format(f'   SORTEANDO {qtdJogos} JOGOS   '))
for q in range(0, qtdJogos):
    jogo = list()
    num = int
    for c in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                break
        if c == 0:
            jogo.append(num)
        else:
            jogo.append(num)
    listaDeJogos.append(jogo[:])
    listaDeJogos[q].sort()
    jogo.clear()
    print(f'Jogo {q + 1}:{listaDeJogos[q]}')
    sleep(0.5)
print('{:=^30}'.format('   BOA SORTE   '))
