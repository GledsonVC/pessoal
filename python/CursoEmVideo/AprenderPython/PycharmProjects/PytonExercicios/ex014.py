# Escreva um programa que converta um temperatura digitada em °C e converta para °F.
c = float(input('Informe a temperatura em °C: '))
f = (c * 9 / 5)+32
print('A temperatura de {:.1f}°C corresponde a {:.1}°F!'.format(c, f))
