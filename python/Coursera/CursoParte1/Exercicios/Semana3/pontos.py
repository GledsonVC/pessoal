import math
x1 = int(input("Digite o xa para o primeiro ponto carteseano: "))
y1 = int(input("Digite o ya para o primeiro ponto carteseano: ")) 
x2 = int(input("Digite o xb para o segunto ponto carteseano: "))
y2 = int(input("Digite o yb para o segundo ponto carteseano: ")) 
result = math.sqrt((x1**2 - 2*x1*x2 + x2**2) + (y1**2 - 2*y1*y2 + y2**2))
if result>=10:
    print("longe")
else:
    print("perto")
