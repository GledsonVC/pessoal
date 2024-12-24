# ao igualar uma lista em outra o python cria uma ligação entre as duas listas
# e fazendo uma lista receber todas as listagem de outra
a = [2, 3, 4, 7]
b = a       # igualando e fazendo ligação
c = a[:]    # recebendo apenas os valores
b[2] = 8
c[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
