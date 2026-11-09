print('-='*33)
print('Programa q calcula o preço por quantidade de dois produtos e mostra o mais em conta')
while True:
    s = ' '
    print('-='*33)
    p1 = float(input('Digite o preço do PRIMEIRO produto:\n R$'))
    q1 = float(input('Digite a quantidade em (Kg) ou (L):\n '))
    p2 = float(input('Digite o preço do SEGUNDO produto:\n R$'))
    q2 = float(input('Digite a quantidade em (Kg) ou (L):\n '))
    #calcula preço por Kg ou L
    print('-='*33)
    p1 = p1/q1
    p2 = p2/q2
    if p1==p2:
        print('Produtos com o mesmo valor por (Kg) ou (L)')
    elif p1<p2:
        print('O primeiro produto está com o valor melhor por (Kg) ou (L)')
    else:
        print('O segundo produto está com o valor melhor por (Kg) ou (L)')
    print('Produto 1 = R${:.2f} por (Kg) ou (L)'.format(p1))
    print('Produto 2 = R${:.2f} por (Kg) ou (L)'.format(p2))
    # Saida do loop
    print('-='*33)
    while s not in 'SN':
        s = str(input('Deseja consultar outros produtos? [S/N] : ')).strip().upper()[0]
    if s == 'N':
        break
print('Até mais')

