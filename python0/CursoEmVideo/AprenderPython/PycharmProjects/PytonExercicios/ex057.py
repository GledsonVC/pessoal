# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Sexo [M/F]: ')).strip().upper()
while (sexo != 'M') and (sexo != 'F'):
    print('Codigo inválido, \n[M] para masculino  \n[F] para feminino')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
# Professor fez
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
