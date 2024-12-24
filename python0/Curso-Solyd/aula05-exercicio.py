'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados.
Após isso irá imprimir todos os nomes da lista
'''
print('Programa de controle de convidados 1.0')
print('='*38)
quantidade_de_pessoas = int(input('Qual é a quantidade de pessoas que serão convidadas: '))
lista_de_convidados = []

while quantidade_de_pessoas > 0:
    lista_de_convidados.append(str(input(f'Nome do convidado #{len(lista_de_convidados)+1}: ')))
    quantidade_de_pessoas -= 1

print(f'Serão {len(lista_de_convidados)} Convidado(s)')

print('\nLISTA DE CONVIDADOS:')
for i in range(len(lista_de_convidados)):
    print(f'Convidadado #{i+1}: {lista_de_convidados[i]}')
