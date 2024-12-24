import math

class Bhaskara:
    
    def main(self):
        print("Equação de segundo grau")
        aDig = float(input("Digite um valor para A: "))
        bDig = float(input("Digite um valor para B: "))
        cDig = float(input("Digite um valor para C: "))
        print(self.calculaRaiz(aDig, bDig, cDig))

    def calculaDelta(self, a, b, c):
        return b ** 2 -4 * a * c

    def calculaRaiz(self, a, b, c):
        delta = self.calculaDelta(a, b, c)
        if delta < 0:
            return [0]
        elif delta == 0:
            raiz = (-1*b + math.sqrt(delta)) / (2 * a)
            return [1, raiz]
        else:
            raiz1 = (-1*b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-1*b - math.sqrt(delta)) / (2 * a)
            return [2, raiz1, raiz2]
