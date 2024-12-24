# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~


def escreva(a):
    t = len(a) + 6
    print('~' * t)
    print(f'   {a}')
    print('~' * t)


x = str(input('Digite uma mensagem: '))
escreva(x)
