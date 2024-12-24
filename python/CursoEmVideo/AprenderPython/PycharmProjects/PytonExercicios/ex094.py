# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = list()
cadastro = dict()
media = soma = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        cadastro['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('\033[1;31m  ERRO! Por favor, digite M ou F.\033[m')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    while True:
        cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('\033[1;31m  ERRO! Responda apenas S ou N.\033[m')
    if cont in 'N':
        del cadastro
        break
print('-='*30)
print(f'A) Foram cadastrado um total de {len(pessoas)} pessoas')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C)As mulheres cadastradas foram', end=' ')
for c in pessoas:
    if c['sexo'] in 'F':
        print(c['nome'], end=' ')
print()
print('D) Lista de pessoas que estão acima da média: ')
for c in pessoas:
    if c['idade'] > media:
        print('    ', end='')
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<<ENCERRADO>>>')
