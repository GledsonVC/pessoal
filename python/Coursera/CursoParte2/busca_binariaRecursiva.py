import pytest

def busca_binaria(lista, elemento, min = 0, max = None):
    if max == None:
        max = len(lista) - 1

    if max < min:        
        return False
    else:
        meio = (max + min) // 2

    if lista[meio] >  elemento:
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        
        return meio



lista = [10, 20, 30, 40, 50, 60]

@pytest.mark.parametrize('lista, valor, esperado', [
    (lista, 0, False),
    (lista, 10, 0),
    (lista, 20, 1),
    (lista, 30, 2),
    (lista, 40, 3),
    (lista, 50, 4),
    (lista, 60, 5),
    (lista, 70, False),
    (lista, 15, False),
    (lista, -10, False)    
    ])

def testa_busca_binaria(lista, valor, esperado):
   assert busca_binaria(lista, valor) == esperado 
