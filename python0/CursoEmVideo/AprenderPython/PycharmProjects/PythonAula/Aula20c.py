def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')


contador(1)
contador(1, 2)
contador(1, 2, 3, 4)
contador(1, 2, 3, 4, 5)
