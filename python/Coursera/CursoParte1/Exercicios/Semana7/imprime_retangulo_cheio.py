largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
while altura > 0:
    larguraTemporaria = largura
    while larguraTemporaria > 0:
        print('#', end = '')
        larguraTemporaria -= 1
    altura -= 1
    print()
