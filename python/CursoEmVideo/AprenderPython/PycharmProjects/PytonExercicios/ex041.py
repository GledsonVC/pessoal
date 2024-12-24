# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
nascimento = int(input('Digite o ano de nascimento: '))
from datetime import date
idade = (date.today().year) - nascimento
if idade <= 9:
    print('Categoria MIRIM com {} anos.'.format(idade))
elif idade <= 14:
    print('Categoria INFANTIL com {} anos.'.format(idade))
elif idade <= 19:
    print('Categoria JÚNIOR com {} anos'.format(idade))
elif idade <= 25:
    print('Categoria SÉNIOR com {} anos'.format(idade))
else:
    print('Categoria MASTER com {} anos'.format(idade))
