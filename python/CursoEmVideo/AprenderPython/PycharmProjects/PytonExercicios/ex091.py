# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em
# um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep
jogador = dict()
print('Valores sorteados:')
for c in range(1, 5):
    jogador[f'jogador{c}'] = randint(1, 6)
for k, v in jogador.items():
    sleep(0.5)
    print(f'    O {k} tirou: {v}')
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('Ranking com os jogadores:')
for k, v in enumerate(rank):
    sleep(0.5)
    print(f'    {k+1}º lugar: {v[0]} com {v[1]}')
