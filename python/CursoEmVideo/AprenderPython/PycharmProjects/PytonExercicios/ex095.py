# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome: ')).strip().upper()
    partida = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    jogo = list()
    for p in range(0, partida):
        jogo.append(int(input(f'   Quantos gols na partida {p+1}: ')))
    jogador['gols'] = jogo[:]
    jogador['total'] = sum(jogo)
    time.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
        print('\033[1;31m  ERRO! Por favor responta S ou N.\033[m')
    if cont == 'N':
        break
print('-='*30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    verJogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if verJogador == 999:
        break
    if (verJogador < 0) or (verJogador >= (len(time))):
        print('\033[1;31mERRO! Cod de jogador inválido\033[m')
        print(f'Codigo do jogador está entre 0 e {len(time)-1}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {time[verJogador]["nome"]}')
        for p, g in enumerate(time[verJogador]['gols']):
            print(f'    No jogo {p + 1} fez {g} gols.')
        print('-'*40)
print('<<< Volte sempre >>>')
