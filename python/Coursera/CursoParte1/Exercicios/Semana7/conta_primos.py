def n_primos(n):
    x = 0
    while n >= 2:
        if éPrimo(n) == True:
            x += 1
        n -= 1
    return x        


def éPrimo(k):
    c = 2
    while k > c:
        if k % c == 0:
            return False
        else:
            c = c + 1
    return True

