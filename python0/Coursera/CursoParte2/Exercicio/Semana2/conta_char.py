def conta_letras(frase, contar = 'vogais'):
    vogal = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
    consoante = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
                 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    frase1 = frase.replace(' ', '')
    i = 0
    qtdVogal = 0
    qtdConsoante = 0
    while i < len(frase1):
        if contar == 'vogais' and frase1[i] in vogal:
            qtdVogal += 1                        
        elif contar == 'consoantes' and frase1[i] in consoante:
            qtdConsoante += 1
        i += 1
    if contar == 'vogais':
        return qtdVogal
    elif contar == 'consoantes':
        return qtdConsoante
