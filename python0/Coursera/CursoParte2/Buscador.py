class Buscador():
    def busca_sequencial(self, lista, x):
        '''(list, float) - > bool'''
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1
        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio +1
        return - 1



##import time
##import random
##x = int()
##lista1 = [x for x in range(10000)]
##lista2 = lista1[:]
##busca = Buscador()
##x = 75573
##print('busca_sequencial')
##antesTimeA = time.time()
##print(busca.busca_sequencial(lista1, x))
##fimTimeA = time.time()
##print(f'Tempo: {fimTimeA - antesTimeA}')
##print()
##print('busca_binaria')
##antesTimeB = time.time()
##print(busca.busca_binaria(lista2, x))
##fimTimeB = time.time()
##print(f'Tempo: {fimTimeB - antesTimeB}')


