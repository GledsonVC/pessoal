def soma(numero1, numero2):
    resp = float(numero1 + numero2)
    return resp


def imprime_oi():
    print('Oi')


def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False



print(soma(12.35, 75.60))

imprime_oi()

print(tem_sete_itens('oi pessoal'))
if tem_sete_itens('Gledson'):
    print('Realmente Gledson contem sete letras')

print(tem_sete_itens([1,2,3,4,5,6,7]))

'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior número dentro dessa coleção,
faça outra função que retorna o menor número.
'''

