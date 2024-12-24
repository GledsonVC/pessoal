num = int(input("Digite o valor de n: "))
fat = 1
if num == 0:
    print(fat)
else:
    while num != 1:
        fat = fat * num
        num = num - 1
    print(fat)

