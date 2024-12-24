def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

def somaMais(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(b=2, a=5)  # é a mesma coisa que o soma(5, 4) porem informando A e B invertido
# retorno:
# A = 5 e B = 2
# A soma de A + B = 7
# A = 5 e B = 2
# A soma de A + B = 7

somaMais(5,2)
somaMais(5, 2, 3)
# retorno:
# Somando os valores (5, 2) temos 7
# Somando os valores (5, 2, 3) temos 10
