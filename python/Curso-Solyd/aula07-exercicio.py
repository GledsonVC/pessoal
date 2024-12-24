'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior número dentro dessa coleção,
faça outra função que retorna o menor número.
'''


def colecao_de_numero():
    numero_inicial_lista = int(input('Digite um número para a sua lista: '))
    lista_coleção_de_numeros = [numero_inicial_lista]
    while True:
        if continua():
            lista_coleção_de_numeros.append(int(input('\nDigite mais um número para atribuir a lista: ')))
        else:
            break
    return (lista_coleção_de_numeros)


def continua():
    print('Deseja continuar colocando número na lista?')
    condicao = int(input('    |1|-Para sim\n    |2|-Para não\nSUA OPÇÃO: '))
    while condicao not in (1, 2):
        print(f'Condição {condicao} inválida')
        condicao = int(input('Digite:\n    |1|-Para sim\n    |2|-Para não\n'))
    if condicao == 1:
        return True
    else:
        return False


def maior_numero_lista(lista):
    maior_numero = lista[0]
    for item in lista:
        if maior_numero < item:
            maior_numero = item
    return maior_numero


def menor_numero_lista(lista):
    menor_numero = lista[0]
    i = 0
    while i < len(lista):
        if menor_numero > lista[i]:
            menor_numero = lista[i]
        i += 1
    return menor_numero


print('Programa de Lista de números. \n')
lista = colecao_de_numero()
print('Sua lista ficou assim:\n    ', lista)
print('O Maior número da sua lista é: ', maior_numero_lista(lista))
print('O menor número da sua lista é: ', menor_numero_lista(lista))
