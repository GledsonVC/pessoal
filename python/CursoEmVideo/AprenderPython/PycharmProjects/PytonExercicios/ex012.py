#   Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
#   com 5% de desconto.
p = float(input('Digite o preço do produto: R$'))
print('O preço do produto R${:.2f} com 5% de desconto é R${:.2f}'.format(p, p - (p * (5 / 100))))
