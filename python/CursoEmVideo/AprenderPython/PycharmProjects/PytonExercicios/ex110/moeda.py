def aumenta(num=0, taxa=0, formato=False):
    """
    ->Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param num: o preço que se quer reajusatar.
    :param taxa: qual a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = num+((num*taxa) / 100)
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num-((num*taxa) / 100)
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')


def resumo(num=0, aum=0, red=0 ):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Medade do preço: \t{metade(num, True)}')
    print(f'{aum}% de aumento: \t{aumenta(num, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(num, red, True)}')
    print('-' * 30)

