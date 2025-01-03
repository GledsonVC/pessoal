def leiaDinheiro(num):
    valido = False
    while not valido:
        entrada = str(input(num)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor
