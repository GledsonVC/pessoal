import uteis
from uteis import numeros

n = int(input('Digite um valor: '))
fat = uteis.numeros.fatorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O dobro de {n} é {uteis.numeros.dobro(n)}')
print(f'O triplo de {n} é {uteis.numeros.triplo(n)}')
print(f'O triplo de {n} é {numeros.triplo(n)}')     # Tambem pode ser usado dessa forma se
                                                    # importar com from de uteis do pacote numero
