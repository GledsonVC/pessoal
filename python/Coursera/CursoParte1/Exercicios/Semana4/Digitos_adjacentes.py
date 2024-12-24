n = int(input("Digite um número inteiro: "))
resultado = "não"
while n != 0:
    resto1 = n % 10
    resto2 = (n // 10) % 10
    if resto1 == resto2:
        n = 0
        resultado = "sim"
    else:
        n = n // 10
print(resultado)
