# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.
exp = str(input('Digite a expressão: '))
pilha = list()
for par in exp:
    if par == '(':
        pilha.append(par)
    elif par == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(par)
            break
if len(pilha) == 0:
    print('Expressão Correto')
else:
    print('expressão Incorreta')
