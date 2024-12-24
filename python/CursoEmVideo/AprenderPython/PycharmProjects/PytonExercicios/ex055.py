# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if pesoMaior <= peso:
            pesoMaior = peso
        if  pesoMenor >= peso:
            pesoMenor = peso
print('O maior peso lido foi {}Kg'.format(pesoMaior))
print('O menor peso lido foi {}Kg'.format(pesoMenor))
