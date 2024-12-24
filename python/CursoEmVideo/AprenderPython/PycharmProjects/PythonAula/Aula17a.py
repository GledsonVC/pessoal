num = [2, 5, 9, 1]      # declarando uma Lista
num[2] = 3              # incluindo na posição 2 o 3
num.append(7)           # adcionando um numero a lista
num.sort()              # ordenando a lista
num.sort(reverse=True)  # ordenando invertido
num.insert(2, 0)        # inserindo na posição 2 um 0
num.pop()               # removendo o 1 no final
num.pop(2)              # remove o 0 da posição 2
num.insert(2, 2)        # inserindo outro 2 na posição 2
num.remove(2)           # remove o primeiro 2 que tiver na posição menor da lista
# verificar na lista se contem o numero 4 para depois remover se houver, ou print que não achou
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o valor 4')

print(num)
print(f'Essa lista tem {len(num)} elementos')
