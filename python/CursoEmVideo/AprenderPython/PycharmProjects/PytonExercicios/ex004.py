#Recebe um valor e verifica se é um numero, alfabético, alfanumérico, maiúscula,
#minúscula, se é só um espaço, ou é um nome próprio com letra inicial maiúscula e o resto mínusculo
n = input('Digite algo')
print('O tipo primitivo desse valor é', type(n))

print('É um número? ', n.isnumeric())
print('É uma alfabético? ', n.isalpha())
print('É alfanumerico? ', n.isalnum())
print('Só tem maiúsculas', n.isupper())
print('Só tem minúsculas', n.islower())
print('Só tem espaço? ', n.isspace())
print('Esta como nome próprio', n.istitle())
