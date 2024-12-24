# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
time = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo', 'Santos',
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
        'Vasco da Gama', 'América Mineiro', 'Sport', 'Vitória', 'Paraná')
print(f'Lista de times do Brasileirão 2018: {time}')
print(f'Os 5 primeiros times foram: {time[:5]}')
print('Os 4 úlmos colocados foram: {}'.format(time[-4:]))
print(sorted(time))
print('O Chapecoense está na {}ª posição'.format(time.index('Chapecoense')+1))
