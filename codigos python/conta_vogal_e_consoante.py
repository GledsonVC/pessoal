def conta_letras(frase, contar='vogais'):
    vogal = ['a' , 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase1 = frase.replace(' ', '')
    i = 0
    qtdVogal = 0
    qtdConsoante = 0
    while i < len(frase1):
        carac = frase1[i]
        if carac in vogal:
            qtdVogal += 1
        else:
            qtdConsoante += 1
        i += 1
    if contar == 'vogais':
        return qtdVogal
    elif contar == 'consoante':
        return qtdConsoante

a = str('Oi tudo bem?')
b = 'consoante'
print(conta_letras(a))
print(conta_letras(a, b))
