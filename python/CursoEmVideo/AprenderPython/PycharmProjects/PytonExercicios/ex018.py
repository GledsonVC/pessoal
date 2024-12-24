# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a = float(input('Digite o angulo que vc deseja: '))
print('O angulo de {} tem o seno de {:.2f}'.format(a, sin(radians(a))))
print('O angulo de {} tem o coseno de {:.2f}'.format(a, cos(radians(a))))
print('O angulo de {} tem a tangente de de {:.2f}'.format(a, tan(radians(a))))
