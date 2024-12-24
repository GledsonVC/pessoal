def menor_nome(nomes):
    menor = nomes[0].strip()
    i = 1
    while i < len(nomes):
        nome = nomes[i].strip()
        if len(menor) > len(nome):
            menor = nome            
        i += 1
    return menor.capitalize()
