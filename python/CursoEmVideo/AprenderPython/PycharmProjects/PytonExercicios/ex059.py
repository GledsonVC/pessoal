# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = True
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida, tente novamente')
    print('-='*20)
    sleep(1)
print('Fim do programa! Volte sempre!')
