n = int(input("Digite um número inteiro: "))
result = "primo"
if n >= 2:
    x = 2
    while (x < n) and (result == "primo"):
        if n % x == 0:
            result = "não primo"
        x = x + 1
else:
    if n <= 1:
       result = "não primo"
print(result)
