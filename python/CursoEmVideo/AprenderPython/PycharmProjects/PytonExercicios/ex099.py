# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    print('-=' * 30)
    cont = maior = 0
    print('Analisando os números passados...')
    sleep(2)
    for valor in num:
        sleep(0.5)
        print(f'{valor} ',  end='', flush=True)
        if cont == 0:
            maior = valor
        elif maior <= valor:
            maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
