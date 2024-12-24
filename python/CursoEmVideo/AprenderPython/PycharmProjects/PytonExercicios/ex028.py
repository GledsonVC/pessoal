# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador pensar entre 0 e 5
print('-=-' * 17)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 17)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('Processando...')
sleep(3)
if computador == jogador:
    print('PARABÉNS! Você conseguiu me venceu!')
else:
    print('GUANHEI! Eu pensei no número {} e não no {}! Perdeu!'.format(computador, jogador))
