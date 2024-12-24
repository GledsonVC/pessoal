#   Escreva um programa que leia um valor em metros e o exiba convertido
#   em centimetros e milimetros.
n = float(input('Digite a o metro: '))
print('{} metros equivalem a {:.0f} centímetros'.format(n, n*100))
print('{} metros equivalem a {:.0f} milímetros'.format(n, n*1000))
# desavio extra fazer o mesmo exercício nas escalas
# km hm dam m dm cm mm
m = float(input('Uma distância em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('Uma medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'
      .format(m, km, hm, dam, dm, cm, mm))
