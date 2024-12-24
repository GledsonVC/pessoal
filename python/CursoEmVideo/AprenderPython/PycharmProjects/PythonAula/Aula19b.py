estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()
