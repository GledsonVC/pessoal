def é_hipotenusa(n):
    i = 1
    while i < n:
        j = 1
        while j < n:
            if n == (i ** 2 + j ** 2)** 0.5:
                return True
            j += 1
        i += 1
    return False

    
def soma_hipotenusas(n):
    soma = 0
    cont = 1
    while cont <= n:
        if é_hipotenusa(cont):
            soma += cont
        cont += 1
    return soma
