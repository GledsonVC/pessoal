# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
mediaIdade = 0
nomeVelho = 'SEM REGISTRO'
idadeVelho = 0
mulherAte20 = int(0)
for c in range(1, 5):
    print('{:-^20}'.format('{}ª PESSOA'.format(c)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    mediaIdade = mediaIdade + idade
    if (sexo == 'M') and (idade > idadeVelho):
        nomeVelho = nome
        idadeVelho = idade
    if (sexo == 'F') and (idade < 20):
        mulherAte20 += 1
mediaIdade = mediaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulherAte20))
