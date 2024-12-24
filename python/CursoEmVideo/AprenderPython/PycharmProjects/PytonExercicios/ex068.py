# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
vitoria = 0
while True:
    resultado = ['PAR', 'ÍMPAR']
    maquina = randint(0, 10)
    jogador = int(input('Diga o valor: '))
    soma = (jogador + maquina)
    while True:
        parimpar = str(input('Par ou Ímpar: [P/I]')).strip().upper()[0]
        if parimpar == 'P':
            escolha = 0
            break
        if parimpar == 'I':
            escolha = 1
            break
    print('-'*30)
    print(f'Você jogou {jogador} e a maquina {maquina}. Total de {soma} deu {resultado[soma%2]}')
    print('-'*30)
    if escolha == (soma % 2):
        vitoria+=1
        print('Você VENCEU!')
    else:
        print('VOCÊ PERDEU!')
        break
    print('Vamos jogar novamente...')
print('-='*30)
print(f'GAME OVER! Você venceu {vitoria} vezes.')

# Maneira do professor
print('\n\nMetodo do professor')
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')