# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.
aluno = list()
while True:
    nome = str(input('Nome: ').strip().upper())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print('='*41)
print(f'{"Nº":<3}{"NOME":<30}{"MÉDIA":>8}')
print('-'*41)
for n, a in enumerate(aluno):
    print(f'{n:<3}{a[0]:<30}{a[2]:>8.1f}')
print('='*41)
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        print('FINALIZANDO...')
        break
    if num <= len(aluno) - 1:
        print(f'Notas de {aluno[num][0]} são {aluno[num][1]}')
print('<<< VOLTE SEMPRE >>>')
