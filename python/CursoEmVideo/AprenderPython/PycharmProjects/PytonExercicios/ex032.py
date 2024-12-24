# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o atual: '))
if ano == 0:
    from datetime import date
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    b = 'é BISSEXTO'
else:
    b = 'NÃO é BISSEXTO'
print('O ano {} {}'.format(ano, b))

