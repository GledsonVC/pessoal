# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome Completo:\n')).strip()
primeiro = nome.split()
ultimo = nome.split()
print('Seu primeiro nome é: {}'.format(primeiro[0]))
print('Seu ultimo nome é: {}'.format(ultimo[len(ultimo)-1]))
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu ultimo nome é: {}'.format(nome.split()[len(nome.split())-1]))


