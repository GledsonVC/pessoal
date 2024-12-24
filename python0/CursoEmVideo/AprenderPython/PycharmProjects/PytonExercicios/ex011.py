#   Faça um programa que leia  a largura e a altura de uma parede em metros,
#   calcule a sua área e a quantidade de tinta necessária para pintá-la,
#   sabendo que cada litro de tinta, pinta uma área de  2m²
x = float(input('Qual é a largura da parede em metros?\n'))
y = float(input('Qual é a alttura da parede em metros?\n'))
area = x*y
print('Com a parede {}x{} você tem um área de {}m² e são necessários {:.3f}L de tinta para pintá-la'
      .format(x, y, area, (area/2)))
