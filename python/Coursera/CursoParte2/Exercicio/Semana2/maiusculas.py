def maiusculas(frase):
    frase1 = ''
    i = 0
    while i < len(frase):
        if ehMaiuscula(frase[i]):
            frase1 += frase[i]
        i += 1
    return frase1

def ehMaiuscula(caracter):
    letra = ord(caracter)
    ## na função ord ele irá verificar se no ASCII é letras maiusculas
    if letra >= 65 and letra <= 90:
        return True
    else:
        return False
