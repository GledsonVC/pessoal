# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.33,
         'Livro', 34.9)
print('-'*30)
print('{: ^30} '.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<20}', end='')
    print(f'R${lista[c+1]:5.2f}')
print('-'*30)
