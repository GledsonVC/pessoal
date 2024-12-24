print('\033[0;33;44mOlha a cor como ficou a cor\033[m\n\n\n')
#testes de áula
print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste')
print('\033[30;42mTeste')
print('\033[mTeste')
print('\033[7;30mTeste')
print('\033[m\n')

# Exemplo de variavel
a = 3
b = 5
print('O valor são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# Exemplo dentro do format para não confundir no print
nome = 'Gledson'
print('Muito prazer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('\n\n')

#Exemplo criando variável formando biblioteca
cores = {'limpa': '\033[m',
         'azul': '\033[33m',
         'vermelho': '\033[31m',
         'pretoEBranco': '\033[7:30m'}
nome1 = 'Gledson'
nome2 = 'Ellen'
nome3 = 'Luan'
print('Meu nome é {}{}{}, minha esposa se chama {}{}{} e meu filho {}{}{}.'
      .format(cores['azul'], nome1, cores['limpa'],
              cores['vermelho'], nome2, cores['limpa'],
              cores['pretoEBranco'], nome3, cores['limpa']))
