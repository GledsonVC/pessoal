import time


def abre_arquivo():
    try:
        arquivo = open('arquivodoido.txt')
        print('arquivo encontrado')
        return True
    except Exception as erro:
        print(f'Arquivo não encontrado: {erro}')
        arquivo = open('arquivodoido.txt', 'w')
        return False


while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

arquivo = open('arquivodoido.txt', 'a')
while True:
    print('Gostaria de adicionar algo no arquivo?')
    resposta = int(input(('|1| Para SIM, |2| Para NÃO\n')))
    if resposta not in (1,2):
        print('Opção inválida')
    elif resposta == 1:
        escreve = str(input('Escreva o que deseja incluir no arquivo: '))
        arquivo.write(f'{escreve}\n')
        print('Escrito e salvo com sucesso')
    else:
        break

arquivo = open('arquivodoido.txt', 'r')
print(arquivo.read())
print('Fim do programa')
