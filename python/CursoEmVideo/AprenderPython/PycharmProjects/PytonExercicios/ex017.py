# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, pow, hypot
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
h = sqrt(((pow(co, 2)) + (pow(ca, 2))))
print('A hipotenusa de:\n CO = {} \n CA = {} \né igual a\n H = {:.2f}'.format(co, ca, h))
h: hypot(co, ca)
print('Hipotenusa usando biblioteca hypot do python: {:.2f}'.format(h))
print('print com a função hypot no format\n{:.2f}'.format(hypot(co, ca)))
