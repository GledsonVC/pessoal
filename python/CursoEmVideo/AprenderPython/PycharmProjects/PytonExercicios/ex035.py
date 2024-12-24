# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.
print('-=-' * 17)
print('Analisador de Triângulos')
print('-=-' * 17)
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if (a+b>c) and (b+c>a) and (a+c>b):
    print('Os seguimentos acima PODEM FORMAR triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')
