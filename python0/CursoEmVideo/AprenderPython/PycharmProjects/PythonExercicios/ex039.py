# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# ano = int(input('Ano de nascimento: '))
# ao ver o exercício foi sugestionado a questão do sexo, se for feminino tratar
print('''[ 1 ] para MASCULINO
[ 2 ] para FEMININO''')
sexo = int(input('Sexo: '))
if sexo == 2:
    print('Você não precisa se alistar')
elif sexo == 1:
    from datetime import date
    anoAtual = int(date.today().year)
    anoNascimento = int(input('Ano de nascimento: '))
    idade = int(anoAtual - anoNascimento)
    print('Quem nasceu no ano de {} tem {} anos em {}'.format(anoNascimento, idade, anoAtual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        print('Ainda falta {} anos para o alistamento'.format(18-idade))
        print('Seu alistamento será em {}.'.format(anoAtual+18-idade))
    else:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(anoAtual-idade+18))
else:
    print('Sexo inválido, tente novamente')