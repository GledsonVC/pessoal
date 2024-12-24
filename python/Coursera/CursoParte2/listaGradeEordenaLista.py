##Exercício 1: Gerando listas grandes
##
##Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista
##contendo n números inteiros aleatórios.
##
##Exercício 2: Ordenação com selection sort
##
##Implemente a função ordena(lista), que recebe uma lista com números inteiros como parâmetro e devolve
##esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.
import random
def lista_grande(n):
    lista = []
    for i in range(n):        
        lista.append(random.randint(-n * 100, n*100))
    return lista

def ordena(lista):
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


