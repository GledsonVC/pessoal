tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo'if tempo <= 3 else 'Carro velho')
print('--Fim--')

nome = str(input('Qual seu nome?')).strip()
if nome == 'Gledson':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
