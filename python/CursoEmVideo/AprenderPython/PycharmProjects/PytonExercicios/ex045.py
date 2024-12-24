# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('''
Sua opções:
[ 0 ]PEDRA    [ 1 ]PAPEL    [ 2 ]TESOURA''')
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
j = int(input('Qual a sua jogada? '))
c = int(randint(0, 2))
print('JO'.format(), end='')
sleep(1)
print('KEM'.format(), end='')
sleep(1)
print('PO!!!')
print('-=' * 40)
print('Computador jogou: {}'.format(jogadas[c]))
print('Jogador jogou:    {}'.format(jogadas[j]))
print('-=' * 40)
# LOGICA E PRINT NA TELA PARA VER QUEM GANHOU
if j == c:
    print('\033[7;37;40mEMPATE')
elif (j == 0 and c == 1) or (j == 1 and c == 2) or (j == 2 and c == 0):
    print('\033[;31mCOMPUTADOR VENCE')
elif (j == 0 and c == 2) or (j == 1 and c == 0) or (j == 2 and c == 1):
    print('\033[;32mJOGADOR VENCE')
else:
    print('\033[;31mCOMPUTADOR VENCE')
