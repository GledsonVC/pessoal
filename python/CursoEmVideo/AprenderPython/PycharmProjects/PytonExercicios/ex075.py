# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = (int(input('Digite um número: ')),
         int(input('Digite outro númeor: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
# Mostrando tupla
print(f'Você digitou os valores {tupla}')
# A: quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
# B: Em que posição foi digitado o primeiro valor 3.
if 3 in tupla:
    print(f'O valor 3 foi digitado na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
# C: Quais foram os números pares.
print('O valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
