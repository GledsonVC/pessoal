import re
import requests


# 1
string_de_teste = 'o gato é bonito'
padrao = re.search(r'gat', string_de_teste) #Encontra se contem (gat) em qualquer lugar do padrão regular
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

# 2
string_de_teste = 'o gata é bonito'
padrao = re.search(r'gat.', string_de_teste) #Encontra qualquer padrão por exemplo se fosse (gata) tbm encontraria
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

# 3
string_de_teste = 'o gato é bonito'
padrao = re.search(r'\w\w\w\w\w', string_de_teste)
# \w um caracter que fosse letra de a-Z incluindo (_) mas não espaço no caso 5 letras na string
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado')

# 4
string_de_teste = 'gledsonvc@gmail.com'
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', string_de_teste)
# encontra por padrões de e-mail
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')

# 5
requisicao = requests.get('http://pudim.com.br')
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
# encontra por padrões de e-mail
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')