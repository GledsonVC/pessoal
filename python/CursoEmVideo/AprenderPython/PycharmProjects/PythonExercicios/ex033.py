# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verifica quem é menor
if a < b:
    menor = a
else:
    menor = b
if c < menor:
    menor = c
# Verifica quem é maior
if a > b:
    maior = a
else:
    maior = b
if c > maior:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
