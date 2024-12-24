def soma_matrizes(m1, m2):
    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        
        matrizSoma = []
        for i in range(len(m1)):
            linha  = []
            for j in range(len(m2[i])):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            matrizSoma.append(linha)
        return matrizSoma

    else:
        return False
