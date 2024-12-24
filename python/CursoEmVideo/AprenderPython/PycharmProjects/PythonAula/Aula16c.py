lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


# pode tbm fazer assim
print('\nDe oura maneira com resultado igual')
for cont, comida in enumerate(lanche):  # cont, para fazer contagem junto a enumerate
    print(f'Eu vou comer {comida} na posição {cont}')

print(sorted(lanche)) # irá mostrar a tupla de forma alfabética não mudando nada na tupla
print(lanche)

