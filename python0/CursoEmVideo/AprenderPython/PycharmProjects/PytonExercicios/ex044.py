# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Preço do produto: R$'))
print('''Forma de pagamento:
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
forma = int(input('Qual a opção? '))
if forma == 1:
    total = preco - (preco * (10/100))
elif forma == 2:
    total = preco - (preco * (5/100))
elif forma == 3:
    total = preco
    parcela = 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(total/parcela))
elif forma == 4:
    parcela = int(input('Quantas parcelas?'))
    total = preco + (preco *(20/100))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, total/parcela))
else:
    total = preco
    print('Opção inválida de pagamento, tente novamente')
print('Sua compra é de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
