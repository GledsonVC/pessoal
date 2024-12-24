def leiaInt(num=''):
    while True:
        try:
            ni = int(input(num))
        except:
            print(f'\033[0;31mErro: por favor, digite um número INTEIRO válido.\033[m')
            continue
        else:
            return ni


def linha(tam = 42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
