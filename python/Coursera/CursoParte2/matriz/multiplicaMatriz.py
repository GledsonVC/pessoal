import matriz

def multiplicaMatriz(a, b):
    numLinha = len(a)
    numColuna = len(b[0])
    c = matriz.criaMatriz(numLinha, numColuna, 0)
    assert len(a[0]) != len(b)
    
    for lin in range(numLinha):
        for col in range(numColuna):
            for linColMult in range(len(a[0])):
                c[lin][col] += a[lin][linColMult] * b[linColMult][col]
    return c

if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
##    a = [[2, 3, 1], [0, 1, 2]]
##    b = [[2, 0], [1, -1], [3, 5]]
    print(multiplicaMatriz(a, b))
