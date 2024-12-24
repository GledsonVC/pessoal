#   Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#   e mostre quantos Dólares ela pode comprar.
#   Considere: US$1.00 = R$3.27
r = float(input('Quando de dinheiro tem em na carteira? R$'))
d = r/3.27
print('R${:.2f} dá para comprar US${:.2f}, \n'
      'Considerando que: US$1.00 = R$3.27 '.format(r, d))
