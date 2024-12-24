def criaMatriz(numLinha, numColuna, valor):
    '''(int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com numLinhas linhas e
    numColunas colunuas em que cada elemento é igual
    o valor dado.
    '''
    matriz = [] # lista vazia
    for i in range (numLinha):
        # cria a linha i
        linha = [] # lista vazia
        for j in range (numColuna):
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)

    return matriz
