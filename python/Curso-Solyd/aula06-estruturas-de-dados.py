minha_lista = ['Gui', 'João']                           # LIST
minha_tubla = ('Gui', 'João')                           # TUPLE
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}     # DICT
meu_conjunto = {'Gui', 'João'}                          # SET

print(minha_tubla)
print(minha_tubla[0])
for nome in minha_tubla:
    print(nome)

if 'Gui' in minha_tubla:
    print('Gui está na colecao')

print(meu_dicionario)
print(meu_dicionario['nome'])
print(len(meu_dicionario))
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no dicionário')
for valores in meu_dicionario.values():
    print(valores)
for valores in meu_dicionario.keys():
    print(valores)
meu_dicionario['endereco'] = 'Av. João das Neves'
meu_dicionario['telefone'] = '99999-66666'
print(meu_dicionario)

print(meu_conjunto)
meu_conjunto.add('Maria')
meu_conjunto.add('Gui')
print(meu_conjunto)
meu_conjunto.remove('Gui')
print(meu_conjunto)

#criar variavel vazia
lista = []
tupla = ()
dicionario = {}
conjunto = set()

loucura = [(1,2), (3,4), (5,6), {'nome': 'Gardenal'}, ({'João', 'Maria'}, {'Gabriel'})]
print(loucura)
print(loucura[3]['nome'])
print(loucura[4])
print(len(loucura))
