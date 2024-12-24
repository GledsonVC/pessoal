# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade: ')).strip()
primeiro = cidade.upper().split()
print('SANTO' in primeiro[0])

# Maneira do professor
print(cidade[:5].upper() == 'SANTO')
