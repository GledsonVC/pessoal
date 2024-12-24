nome = 'Gledson'
idade = 39
altura = 1.70

print(nome, 'tem', idade, 'ano de', altura, 'de altura.')
#errado
print(nome + 'tem' + str(idade) + 'ano de' + str(altura) + 'de altura.')
#certo
print(nome + ' tem ' + str(idade) + ' ano de ' + str(altura) + ' de altura.')
#melhorado
frase = nome + ' tem ' + str(idade) + ' ano de ' + str(altura) + ' de altura.'
print(frase)
print(type(frase))

nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura ')
#observe que tudo virou string
print(nome, 'tem', idade, 'ano de', altura, 'de altura.')

numero1 = 27
numero2 = 53
resultado = numero1 + numero2
print(resultado)

'''
EXERCICIO: Faça um foormulario que pergunte
o nome, cpf, endereço, idade, altura e telefone
e imprima isso em um relatório organizado
'''
