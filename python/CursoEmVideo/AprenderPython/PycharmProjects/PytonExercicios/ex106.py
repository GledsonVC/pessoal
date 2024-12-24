# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante:
# use cores.
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;42m',   # 1 - verde
     '\033[0;30;44m',   # 2 - azul
     '\033[0;30;41m',   # 3 - vermelho
     '\033[7;30m'       # 4 - branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    t = len(msg) + 2
    print(c[cor], end='')
    print('~' * t)
    print(f' {msg}')
    print('~' * t)
    print(c[0], end='')
    sleep(1)


# Programa
while True:
    titulo('SISTEMA DE AJUDA PYTHON', 1)
    f = str(input('Função ou Biblioteca > '))
    if f.upper() == 'FIM':
        break
    else:
        ajuda(f)
titulo('ATÉ LOGO!', 3)
