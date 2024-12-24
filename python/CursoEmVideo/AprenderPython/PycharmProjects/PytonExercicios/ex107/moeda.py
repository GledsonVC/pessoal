# aumentar(), diminuir(), dobro() e metade().


def aumenta(num, taxa=1):
    res = num+((num*taxa) / 100)
    return res


def diminuir(num, taxa=1):
    res = num-((num*taxa) / 100)
    return res


def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res
