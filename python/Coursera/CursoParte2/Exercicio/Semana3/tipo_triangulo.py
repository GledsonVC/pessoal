class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return int(self.a + self.b + self.c)

    def tipo_lado(self):
        lado1 = self.a
        lado2 = self.b
        lado3 = self.c
        if lado1 == lado2 and lado1 == lado3: ## equilátero (todos os lados iguais)
            return 'equilátero'
        
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3: ## escaleno (todos os lados diferentes)
            return 'escaleno'
        
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: ## isósceles (dois lados iguais)
            return 'isósceles'
