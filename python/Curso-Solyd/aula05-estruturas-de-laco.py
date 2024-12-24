nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']
for nome in nomes:
    print(nome)
print('-='*20)

lista_de_numeros = range(5)
for item in lista_de_numeros:
    print(item)
print('-='*20)

lista_de_numeros = range(5, 10)
for item in lista_de_numeros:
    print(item)
print('-='*20)

lista_de_numeros = range(0, 10, 2)
for item in lista_de_numeros:
    print(item)
print('-='*20)

for i in range(4):
    print(nomes[i])
print('-='*20)

for i in range(len(nomes)):
    print(nomes[i])
print('-='*20)

palavra = 'Gledson Vasconcellos Cavalheiro'
for letra in palavra:
    print(letra)
print('-='*20)

i = 0
while i < 10:
    print('i ainda é menor do que 10: ', i)
    i += 1
print('Acabou o while ', i)
print('-='*20)

numero = 1
while True:
    print(numero)
    if numero == 10:
        break
    numero += 1

'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e 
colocar numa lista de convidados.
Após isso irá imprimir todos os nomes da lista
'''