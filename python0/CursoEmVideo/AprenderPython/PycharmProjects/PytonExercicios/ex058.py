# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.
# OBS desafio 28:
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
c = randint(0, 10)
print('Pensei em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
palpite = int(0)
j = int(11)
while j != c:
    j = int(input('Qual seu palpite?'))
    if j > c:
        print('MENOS... Tente mais uma vez.')
    if j < c:
        print('MAIS... Tente mais uma vez.')
    palpite += 1
print('Parabéns, você acertou mas precisou de {} palpites'.format(palpite))
# professor fez com while false ou true
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpite))
