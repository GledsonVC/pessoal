# importando toda biblioteca math# import math# importando emoji para o ultimo printimport emoji# importando apenas a funçionalidade sqrtfrom math import sqrt, ceil, floor, truncnum = int(input('Digite um número: '))# raiz = math.sqrt(num)raiz = sqrt(num)# print mostrando a raiz simplesprint('A raiz de {} é igual a {:.2f}'.format(num, raiz))# print arredondando para cima# print('A raiz arredondando para cima de {} é igual a {}'.format(num, math.ceil(raiz)))print('A raiz arredondando para cima de {} é itual a {}'.format(num, ceil(raiz)))# print arredondando para baixo# print('A raiz arredondando para baixo de {} é itual a {}'.format(num, math.floor(raiz)))print('A raiz arredondando para baixo de {} é itual a {}'.format(num, floor(raiz)))# print truncando o valor até a virgula# print('A raiz eliminando a virgula sem arredondar de {} é itual a {}'.format(num, math.trunc(raiz)))print('A raiz eliminando a virgula sem arredondar de {} é itual a {}'.format(num, trunc(raiz)))print(emoji.emojize("Olá, mundo de bibliotecas externas :earth_americas:!", use_aliases=True))