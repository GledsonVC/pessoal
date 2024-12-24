# Parametros opcionais
def soma(a=0, b=0, c=0): # nesse caso não informando a, b ou c ele atribui 0 pois é opcional
    s= a+b+c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 4) # aqui não está sendo informado o 'c' por exemplo
soma(b=4, c=2) # aqui não informei o valor para 'a'
soma() # aqui não informei nem a nem b nem c