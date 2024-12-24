# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: \n').strip())
print('A letra "A" aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra "A" apareceu na posição {} da frase.'.format(frase.upper().find('A')+1))
print('A ultima letra "A" apareceu na posição {} da frase.'.format(frase.upper().rfind('A')+1))
