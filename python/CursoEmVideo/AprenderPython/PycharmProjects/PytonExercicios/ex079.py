# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.
listanum = list()
num = int
while True:
    num = int(input('Digite um valor: '))
    if num not in listanum:
        listanum.append(num)
        print('Valor adcionado com sucesso')
    else:
        print('Valor duplicado! Não vou adcionar ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n]: ')).strip().upper()[0]
    if continuar == 'N':
        break
listanum.sort()
print(f'Você digitou os valores: {listanum}')
