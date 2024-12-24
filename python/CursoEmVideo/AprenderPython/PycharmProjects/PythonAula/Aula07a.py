# igual 20 vezes em print
print('='*20)

#Print 1 irá aparecer o nome em 20 caracteres
#print 2 irá aparecer o nome em 20 caracteres porem ele no final
#print 3 irá aparecer o nome em 20 caracteres porem ele no inicio
#print 4 irá aparecer o nome em 20 caracteres porem ele centralizado
nome = input('Qual é o seu nome? ')
print('Prazem em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))

# Operando valores
n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
rd = n1%n2
di = n1//n2
e = n1**n2
# print já somando duas variaveis inteiras e irá mostrar o valor)
print('a soma é: {}'.format(n1+n2))
# print  mostra a variavel da soma
print('a soma é: {}'.format(s))
# print  mostra a variavel da multiplicação
print('o produto é: {}'.format(m))
# print  mostra a variavel da divisão
print('a divisão é: {}'.format(d))
# print  mostra a variavel resto da divisão
print('o resto da divisão é: {}'.format(rd))
# print  mostra a variavel da divisão em valor inteiro
print('a divisão inteiro é: {}'.format(di))
# print  mostra a variavel da potenciação
print('o exponencial é: {}'.format(e))
# print  mostra a variavel da tudo em um print só
print('a soma é {}, o produto é {}, a divisão é {}, o resto da divisão é {}, divisão inteira {} e potencia {}'
      .format(s, m, d, rd, di, e))
# print  mostra a variavel da divisão com apenas 3 casas decimais
print('a divisão com três casas decimais é: {:.3f}'.format(d))
# dois print sem quebra de linha no primeiro print invertendo as variáveis
print('a soma é {2}, o produto é {1}, a divisão é {0},'.format(d, m, s), end=' ')
print('o resto da divisão é {}, divisão inteira {} e potencia {}'.format(rd, di, e))
# print com quebra de linha usando \n
print(' A soma é: {} .\n O produto é: {} .\n A divisão é: {:.2f} .\n O resto da divisão é: {} .\n'
      ' A divisão inteira é: {} .\n A potencia é {} .'.format(s, m, d, rd, di, e))
