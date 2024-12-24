def main():
    carro1 = Carro('Brasília', 1968, 'amarela', 80)
    carro2 = Carro('Fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velMaxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vel = 0
        self.maxVel = velMaxima # velocidade maxima

    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print(f'{self.modelo)} {self.cor} {self.ano}')
        elif self.vel < self.maxVel:
            print(f'{self.modelo} {self.cor} indo a {self.vel} km/h')
        else:
            print(f'{self.modelo} {self.cor} indo muito raaaaaapiiiidoooo!')

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxVel:
            self.vel = self.maxVel
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
