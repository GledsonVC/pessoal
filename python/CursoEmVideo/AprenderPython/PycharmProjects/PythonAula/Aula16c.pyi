lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont, comida in enumerate(lanche):
print(f'Eu vou comer {comida} na posição {cont}')

# pode tbm fazer assim
print('\nDe oura maneira com resultado igual')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
