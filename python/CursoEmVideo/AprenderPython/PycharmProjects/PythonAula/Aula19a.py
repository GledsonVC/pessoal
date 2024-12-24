pessoas = {'nome': 'Gledson',
           'sexo': 'M',
           'idade': 37}
print(pessoas)
# {'nome': 'Gledson', 'sexo': 'M', 'idade': 37}
print(pessoas['nome'])
# Gledson
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# O Gledson tem 37 anos.
print(pessoas.keys())
# dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())
# dict_values(['Gledson', 'M', 37])
print(pessoas.items())
# dict_items([('nome', 'Gledson'), ('sexo', 'M'), ('idade', 37)])

print()
for k in pessoas.keys():
    print(k)
# nome
# sexo
# idade

print()
for v in pessoas.values():
    print(v)
# Gledson
# M
# 37

print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
# nome = Gledson
# sexo = M
# idade = 37

print()
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
# nome = Gledson
# idade = 37

print()
pessoas['nome'] = 'Luan'
for k, v in pessoas.items():
    print(f'{k} = {v}')
# nome = Luan
# idade = 37

print()
pessoas['peso'] = 14
for k, v in pessoas.items():
    print(f'{k} = {v}')
# nome = Luan
# idade = 37
# peso = 14

