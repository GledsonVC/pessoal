# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = maisDeMil = menorPreco = cont = 0
nomeMenorPreco = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maisDeMil += 1
    if (cont == 1) or (preco < menorPreco):
        menorPreco = preco
        nomeMenorPreco = nome
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenorPreco} que custa R${menorPreco:.2f}')
