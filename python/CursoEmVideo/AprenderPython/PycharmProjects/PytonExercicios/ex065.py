# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
sair = ''
num = media = maior = menor = soma = cont = 0
while sair != 'N':
    num = int(input('Digite um número: '))
    sair = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if(cont == 0):
        maior = menor = num
    else:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = menor
    soma += num
    cont += 1
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
