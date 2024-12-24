from random import randint
from time import sleep
contJ = contC = 0
print('VENCE QUEM FIZER 3 PONTOS')
while (contC != 3) and (contJ != 3):
  print('''Jokempo: [1]PEDRA [2]PAPEL [3]TESOURA''')
  jogada = ['JOGADA INVÁLIDA', 'PEDRA', 'PAPEL', 'TESOURA']
  j = int(input('Sua opção? '))
  c = int(randint(1, 3))
  # jokempo em 1 segungo
  print('JO')
  sleep(1)
  print('KEM')
  sleep(1)
  print('PO!!!')
  # Jogada pc e jogador
  print('=='*20)
  print('Maquina jogou: {}'.format(jogada[c]))
  if j==1 or j==2 or j==3 :
    print('Jogador jogou : {}'.format(jogada[j]))
  else:
    j = 0
    print('Jogador jogou : {}'.format(jogada[j]))
    print('=='*20)
  # quem vence
  if j==c:
    print('EMPATOU')
    contJ += 1
    contC += 1
    print('JOGADOR {} x {} MAQUINA'.format(contJ, contC))
  elif j==0:
    contC += 1
    print('JOGADOR {} x {} MAQUINA'.format(contJ, contC))
  elif (j==1 and c==2) or (j==2 and c==3) or (j==3 and c==1):
    contC += 1
    print('JOGADOR {} x {} MAQUINA'.format(contJ, contC))
  elif (c==1 and j==2) or (c==2 and j==3) or (c==3 and j==1):
    contJ += 1
    print('JOGADOR {} x {} MAQUINA'.format(contJ, contC))
print('FIM DO JOGO.')
