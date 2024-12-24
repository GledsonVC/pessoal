# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo:\n')).strip()
print('O nome todo em maiúsculo é {}'.format(nome.upper()))
print('O nome todo em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

# ultimo de quantas letras tem o primeiro nome pode ser
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
primeiro = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro[0], len(primeiro[0])))
