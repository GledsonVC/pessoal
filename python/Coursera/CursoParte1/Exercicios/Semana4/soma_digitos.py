n = int(input("Digite um número inteiro: "))
somaDig = 0
while n != 0:
    somaDig = somaDig + (n % 10)
    n = n // 10
print(somaDig)
        
