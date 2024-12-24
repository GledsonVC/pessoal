# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = 0
maiorSegundaLinha = int()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if c == 2:
            somaTerceiraColuna += matriz[l][c]
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]: ^3}]', end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
for c in range(0, 3):
    if (c == 0) or (matriz[1][c] > maiorSegundaLinha):
        maiorSegundaLinha = matriz[1][c]
print(f'A maior valor da segunda linha é {maiorSegundaLinha}')
