lista = []
x = True
while x:
    n = int(input('Digite um número: '))
    if n != 0:
        lista.append(n)
    else:
        x = False
print()
for i in lista[::-1]:
    print(i)
    

    
