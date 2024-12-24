# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.
jogador = dict()
jogador['nome'] = str(input('nome: ')).strip().upper()
partida = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
jogo = list()
for p in range(0, partida):
    jogo.append(int(input(f'   Quantos gols na partida {p+1}: ')))
jogador['gols'] = jogo[:]
jogador['total'] = sum(jogo)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'    Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
