# Crie  um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples. O sistema só vai ter 2 opções:
# cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
#
# def menu():
#     print('-' * 20)
#     print(f'|{"Opções":^18}|')
#     print('-' * 20)
#     print(' 1 ver cadastro\n 2 cadastrar pessoa\n 3 sair''')
#     print('-' * 20)
#
#
# def opcoes():
#     while True:
#         try:
#             x = int(input('O que deseja? '))
#             if str(x) not in '123':
#                 x = 'erro'
#         except:
#             print('\033[0;31mErro: por favor, digite um 1 ou 2 ou 3.\033[m')
#             continue
#         else:
#             return x
#
#
# def ler():
#     with open('cadastro.txt', 'r') as arquivo:
#         for i in arquivo:
#             i = i.rstrip()
#             print(f'{i: <30}')
#
#
# def cadastrar():
#     cadastro = list()
#     cadastro.append(str(input('Nome: ').strip()))
#     cadastro.append(str(input('Idade: ')))
#     with open('cadastro.txt', 'a') as arquivo:
#         for i in cadastro:
#             arquivo.write(str(i) + ' ')
#         arquivo.write('\n')
#     cadastro.clear()
#
#
# while True:
#     cabeçalho()
#     menu()
#     ret = opcoes()
#     if ret == 1:
#         ler()
#     if ret == 2:
#         cadastrar()
#     if ret== 3:
#         break
# print('OBRIGADO, VOLTE SEMPRE!')
from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq = 'Cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ').strip().capitalize())
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)



