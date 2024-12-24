largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
alturaTemporaria = altura
while altura > 0:
    larguraTemporaria = largura
    while larguraTemporaria > 0:
        if altura == 1 or altura == alturaTemporaria:
            print('#', end = '')
        else:
            if larguraTemporaria == 1 or largura == larguraTemporaria:
                print('#', end = '')
            else:
                print(' ', end = '')
        larguraTemporaria -= 1
    altura -= 1
    print()

