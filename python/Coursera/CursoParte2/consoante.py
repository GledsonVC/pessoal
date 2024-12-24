## Programa que imprime a lista de consoantes maiusculas e minusculas
consoante = []
i = 65
while i <= 90:
    if i != 65 and i != 69 and i != 73 and i != 79 and i !=  85:
        consoante.append(chr(i))
    i += 1
i = 97
while i <= 122:
    if i != 97 and i != 101 and i != 105 and i != 111  and i != 117:
        consoante.append(chr(i))
    i+= 1
print(consoante)

