var_verdade = True
var_falso = False
print(type(var_verdade), type(var_falso))
print(var_falso)

if var_verdade == True:
    print('var_verdade é verdadeiro')

print('\nOutro parte')
a = 2
b = 20

if a > b:
    print(a, 'é maior do que', b)
else:
    print(a, 'Não é maior do que', b)

print('\n Programa opções de menu')
print('\nMenu:\n1 = Carne\n2 = Frango\n3 = Peixe\n')

opcao = input('Escolha a opção: ')

if opcao == '1':
    print('Você escolheu carne')
elif opcao == '2':
    print('Você escolheu frango')
elif opcao == '3':
    print('Voce escolheu peixe')
else:
    print('Opção inválida')


'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual 60 kilos
e medir mais ou igual 1,70 metros
'''
