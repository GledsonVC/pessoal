# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.
# obs do exercício 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela
# a sua tabuada.
n = int(input('Digite um número inteiro: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
