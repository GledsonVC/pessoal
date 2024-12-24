'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual 60 kilos
e medir mais ou igual 1,70 metros
'''


idade = int(input('Qual sua idade: '))
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual é sua altura: '))


if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Apto a entrar no exercito')
else:
    print('Não apto a entrar no exercito')
