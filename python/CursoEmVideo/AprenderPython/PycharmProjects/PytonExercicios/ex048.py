# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.
m = 0
s = 0
for c in range(1, 501, 2):
    if c%3 == 0:
        m = m + 1
        s = s+c
print('A soma de todos os {} valores solicitados é {}'.format(m, s))
