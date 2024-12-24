# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(num=''):
    while True:
        try:
            ni = int(input(num))
        except:
            print(f'\033[0;31mErro: por favor, digite um número INTEIRO válido.\033[m')
            continue
        else:
            return ni


def leiaFloat(num=''):
    while True:
        try:
            nr = float(input(num))
        except:
            print('\033[0;31mErro: por favor, digite um número REAL válido.\033[m')
            continue
        else:
            return nr


i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O numero Inteiro foi {i} e o número Real foi {r}')
