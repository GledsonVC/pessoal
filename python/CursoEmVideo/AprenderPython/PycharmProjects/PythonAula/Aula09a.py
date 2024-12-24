frase = 'Curso em Vídeo Python'
print(frase)
print('012345678901234567890')
print('          1         2')
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
# Analise de string
print(frase.count('o'))
print(frase.count('O'))
# Transformação + Analise
print(frase.upper().count('O'))

# Analise frase2 com espaços
frase2 = '   Curso em Vídeo Python  '
print(frase2)
print('01234567890123456789012345')
print('          1         2     ')
print(len(frase2))
# Transformação + Analise
print(len(frase2.strip()))

# Transformação da frase
print(frase.replace('Python', 'Android'))

# Mudando a frase
frase = frase.replace('Python', 'Android')
print(frase)
frase = frase.replace('Android', 'Python')

# Analise
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
fraseDividida = frase.split()
print(fraseDividida)
print(fraseDividida[0])
print(fraseDividida[2])
print(fraseDividida[2][3])

print('\n{}'.format(frase))
print('{}'.format(frase2))



# print com msg longa
print('''\n
De tudo, ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.

Quero vivê-lo em cada vão momento
E em louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento.

E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, fim de quem ama

Eu possa me dizer do amor (que tive):
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure.
''')