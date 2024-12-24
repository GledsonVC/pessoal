# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
import math
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos deseja pagar a casa? '))
prestacao = valor / (anos * 12)
print(prestacao)
a = str
if (prestacao > ((salario * 30) / 100)):
    a = 'NÃO APROVADO'
else:
    a = 'APROVADO'
print('A casa no valor de R${} ficará com prestação de R${:.2f} ao mês'.format(valor, prestacao))
print('Emprestimo {}!'.format(a))
# explicando ele cria a variável minimo para comparar no if
minimo = salario * 30 / 100
if(prestacao <= minimo):
    print('Emprestimo  não consedido')
else:
    print('Emprestimo consedido')
