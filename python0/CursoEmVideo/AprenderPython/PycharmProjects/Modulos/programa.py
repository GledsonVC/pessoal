import uteis
from uteis import triplo  # pode importar assim tem conforme já estudamos

n = int(input('Digite um valor: '))
fat = uteis.fatorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O dobro de {n} é {uteis.dobro(n)}')
print(f'O triplo de {n} é {uteis.triplo(n)}')
print(f'O triplo de {n} é {triplo(n)}')  # Tambem pode ser usado dessa maneira depois do from
