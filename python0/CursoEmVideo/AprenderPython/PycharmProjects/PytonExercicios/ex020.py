# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample, shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
print('A ordem de apresentação de trabalho é: \n{}'.format(sample([a, b, c, d], 4)))

# Escolha do professor foi suffle para embaralhar segue com as mesmas variáveis, incluindo uma a mais
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação do professor será: \n{}'.format(lista))
