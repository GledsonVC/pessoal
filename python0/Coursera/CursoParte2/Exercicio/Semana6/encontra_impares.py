def encontra_impares(lista):
    listaImpar = []
    if (len(lista) == 1):
        if (lista[0] % 2 == 0):
            return listaImpar
        return lista
    else:
        if lista[0] % 2 == 0:
            return encontra_impares(lista[1:])
        else:
            listaImpar.extend([lista[0]])
            return listaImpar + encontra_impares(lista[1:])
