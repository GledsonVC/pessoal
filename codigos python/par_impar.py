from random import randint
print('\n')
venceu = 0
perdeu = 0
partida = 0
while True:
  maq = randint(1, 2)
  escolha = ' '
  while escolha not in 'PI':
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  jog = int(input('Digite um valor: '))
  soma = maq + jog
  print(f'Eu coloquei {maq}.')
  print(f'E o total somado foi {soma}!')
  if (soma%2) == 0:
    resultado = 'P'
    print('Deu PAR...')
  else:
    resultado = 'I'
    print('Deu ÍMPAR...')
  if (escolha == resultado):
    print('Você GANHOU!')
    venceu += 1
  else:
    print('Você PERDEU!')
    perdeu += 1
  partida +=1
  print('=='*14)
  while escolha not in 'SN':
    escolha = str(input('Vamos jogar novamente? [S/N] ')).strip().upper()[0]
  if escolha == 'N':
    break
print('=='*14)
print(f'Fim de jodo! Você ganhou {venceu} e perdeu {perdeu} em um total de {partida} partida(s)!')
print('=='*14)
if venceu > perdeu:
  print('PARABÉNS, venceu mais que perdeu.')
elif perdeu > venceu:
  print('Que pena q mais perdeu q ganhou, jogue comigo mais tarde.')
else:
  print('EMPATAMOS, a próxima tentarei ganhar!')
