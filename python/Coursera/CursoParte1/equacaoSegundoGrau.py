import math
print("Equação de segundo grau")
a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
delta  = b ** 2 -4 * a * c
if delta < 0:
    print("Não existe raizes reais")
if delta >= 0:
    x1 = (-1*b - math.sqrt(delta)) / (2 * a)
    x2 = (-1*b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("A raiz dessa equação é", x1)
    else:
        print("As raizes dessa equação são", x1, "e", x2)
