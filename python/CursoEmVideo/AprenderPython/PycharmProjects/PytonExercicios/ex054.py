# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoAtual = date.today().year
menor = 0
maior = 0
for c in range(1, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = anoAtual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))
print('E também tivemos {} pessoas maiores de idade'.format(maior))

