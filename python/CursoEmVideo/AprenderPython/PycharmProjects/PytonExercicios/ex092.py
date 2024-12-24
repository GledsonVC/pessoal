# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# obs: para aposentar tem que ter 35 anos de profissão
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).strip().upper()
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Nº Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['anoContrato'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposenta'] = cadastro['idade'] + cadastro['anoContrato'] + 35 - datetime.now().year

print('=-'*30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k:<12} = {v}')