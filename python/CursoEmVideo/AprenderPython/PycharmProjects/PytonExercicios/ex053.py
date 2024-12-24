# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str((input('Digite uma frase: ')).strip().upper())
frase = frase.split()
frase = ''.join(frase)
inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso = inverso + frase[c]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
# Outra maneira sem usar o for
frase = str((input('Digite uma frase: ')).strip().upper())
frase = frase.split()
frase = ''.join(frase)
inverso = frase[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
