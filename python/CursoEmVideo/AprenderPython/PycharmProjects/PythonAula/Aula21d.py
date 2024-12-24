# Retorno de valores
def soma(a=0, b=0, c=0):
    s = a+b+c
    return s


print(soma(3, 2, 5)) # retorna 10

resp = soma(3, 2, 5)
print(resp)         # retorna 10

r1 = soma(3, 2, 5)
r2 = soma(1, 7)
r3 = soma(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')
# retorna
# Meus calculos deram 10, 8 e 4.
