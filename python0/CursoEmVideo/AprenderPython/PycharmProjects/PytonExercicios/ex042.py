# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
'''
OBS: Relembrando o desafio 35.
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''
s1 = int(input('Primeiro seguimento: '))
s2 = int(input('Segundo seguimento: '))
s3 = int(input('Terceiro seguimento: '))
if (s1 > s2+s3) or (s2 > s1+s3) or (s3 > s2+s1):
    print('Os seguimentos acima NÃO PODEM formar um triângulo')
else:
    print('Os seguimentos acima PODEM formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
