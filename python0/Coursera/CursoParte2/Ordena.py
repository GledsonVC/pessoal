class Ordena:
    def selecaoDireta(self, lista):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]

    def bolha(self, lista):
        for i in range(len(lista)-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            
    def bolhaMelhorada(self, lista):
        for i in range(len(lista)-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return

            

import random
import time
def listaGrande(n):
    lista = [1, 2, 3, 5, 4]
##    for i in range(n):
##        lista.append(random.randint(0 , n))
    return lista 



o = Ordena()
a = listaGrande(10000)
b, c = a[:], a[:]

antesTimeA = time.time()
print(a)
print('seleção direta')
o.selecaoDireta(a)
print('resultado = ', a)
fimTimeA = time.time()
print(f'Tempo: {fimTimeA - antesTimeA}')

antesTimeB = time.time()
print(b)
print('bolha')
o.bolha(b)
print('resultado = ', b)
fimTimeB = time.time()
print(f'Tempo: {fimTimeB - antesTimeB}')

antesTimeC = time.time()
print(c)
print('bolhaMelhorada')
o.bolhaMelhorada(c)
print('resultado = ', c)
fimTimeC = time.time()
print(f'Tempo: {fimTimeC - antesTimeC}')
