galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()           # esse comando limpa a lista da variável dados
print(galera)  # Para mostrar os dados inclusos no programa na lista composta galera
# retorno: # [['Maria', 21], ['Paulo', 13], ['Ricardo', 60]]
maior = menor = 0
for c in galera:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{c[0]} é menor de idade.')
        menor += 1
    # for retornando tudo isso:
    # Maria é maior de idade.
    # Paulo é menor de idade.
    # Ricardo é maior de idade.

print(f'Temos no total {maior} maiores e {menor} menores de idade')
# print mostrando os maior e menor de idade
# Temos no total 2 maiores e 1 menores de idade
