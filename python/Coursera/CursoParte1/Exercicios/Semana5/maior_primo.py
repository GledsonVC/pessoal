def maior_primo(x):
    while True:
        if x >= 2 and éPrimo(x):
            return x
        else:
            x = x - 1


def éPrimo(k):
    c = 2
    while k > c:
        if k % c == 0:
            return False
        else:
            c = c + 1
    return True
