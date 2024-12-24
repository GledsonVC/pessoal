nome = str(input('Qual é o seu nome? '))
if nome == 'Gledson':
    print('Que nome bonito!')
elif nome == 'Ellen' or nome == 'Luan':
    print('Você é uma pessoa especial')
elif nome in 'Zoraide Maria Clovis Diniz':
    print('Sem esse nome não haveria uma família linda')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}.'.format(nome))
