def primeiro_lex(lista):
    menorLex = lista[0]
    i = 1
    while i < len(lista):
        if menorLex > lista[i]:
            menorLex = lista[i]
        i += 1
    return menorLex
