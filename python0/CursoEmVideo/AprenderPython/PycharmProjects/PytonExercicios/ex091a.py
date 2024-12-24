from random import randint
from time import sleep
jogador = dict()
listaTemporaria = list()
rank = list()
print('Valores sorteados:')
for i in range(1, 5):
    sleep(0.5)
    jogador["jogador"] = str(f'jogador{i}')
    jogador["dados"] = randint(1, 6)
    print(f'    {jogador["jogador"]} tirou {jogador["dados"]} no dado.')
    listaTemporaria.append(jogador.copy())
print('Ranking com os jogadores:')
sleep(0.5)
# ordenar rank
for c in range(0, len(listaTemporaria)):
    if (c == 0) or (listaTemporaria[c]["dados"] <= rank[-1]["dados"]):
        rank.append(listaTemporaria[c])
    else:
        cont = 0    # acho que é Gambiarra mas não achei outra solução
        while True:
            if (listaTemporaria[c]["dados"]) > rank[cont]["dados"]:
                rank.insert(cont, listaTemporaria[c])
                break
            cont += 1
# Imprime
for c in range(0, len(rank)):
    sleep(0.5)
    print(f'    {c+1}º lugar: {rank[c]["jogador"]} com {rank[c]["dados"]}')
