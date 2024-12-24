import matriz   # importa o cria matriz para criar a matriz no padrão da soma

def somaMatriz(a, b):
    numLinha  = len(a)
    numColuna = len(a[0])
    c = matriz.criaMatriz(numLinha, numColuna, 0)

    for lin in range(numLinha): # percorre as linhada matriz
        for col in range(numColuna): # percorre as colunas da matriz
            c[lin][col] = a[lin][col] + b[lin][col]

    return c

if __name__ == '__main__':
    a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    b = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
    print(somaMatriz(a, b))
