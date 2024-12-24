# Crie um algoritimo que leia um número e mostre o seu
# dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n ** (1 / 2)
print('O numero: {}\n'
      'tem como dobro: {}\n'
      'tem como o triplo: {}\n'
      'sua raiz quadrada: {:.2f}'
      .format(n, d, t, r))
print('Raiz usando comando pow {:.2f}'.format(pow(n, (1/2))))
