frase = 'Oi, tudo bem?'
lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

print(frase)
print(frase[0])
print(lista_nomes)
print((lista_nomes[0]))
print(frase[0:2])
print(frase[0:13:2])
print(lista_nomes[0:2])
print(lista_nomes[0:4:2])
print(frase[-1])
print(lista_nomes[-1])
print(frase[::-1])

lista_nomes.append('Geralda')
print(lista_nomes)
lista_nomes.remove('Geralda')
print(lista_nomes)
lista_nomes.insert(1, 'Creosvaldo')
print(lista_nomes)
lista_nomes[1] = 'João'
print(lista_nomes)
contador_joao = lista_nomes.count('João')
print(type(contador_joao))
print(contador_joao)
print(len(lista_nomes))
print(lista_nomes.pop())
print(lista_nomes)
print(frase.lower())
print(frase)
print(frase.upper())
frase_separada = frase.split(',')
print(frase_separada)
print(frase_separada[1])
frase_nova = frase + ' Como vai você?'
print(frase_nova)

