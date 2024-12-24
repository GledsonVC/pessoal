import requests
import json

requisicao = None


def lista_filmes(titulo_do_filme):
    lista_de_filmes = []
    for i in range(1, 101):
        try:
            requisicao = requests.get(
                'http://www.omdbapi.com/?s=' + titulo_do_filme + '&page=' + str(i) + '&apikey=7bb6880e')
            resposta = json.loads(requisicao.text)
            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    lista_de_filmes.append(filme)
        except Exception as err:
            print('Erro na conexão', err)
            return None
    return lista_de_filmes


def printar_quantidade_filmes(filmes):
    print(f'Contem {len(filmes)} filmes:')


def printar_titulos_das_lista_de_filmes(filmes):
    for titulo in range(len(filmes)):
        print(filmes[titulo]['Title'])
    print('')


def deseja_mais_informacao(filmes):
    while True:
        print('Deseja mais informações sobre algum título?')
        escolha = str(input('Informe o título completo desejado ou |SAIR|: '))
        if escolha in ('sair', 'SAIR'):
            print('Saindo da escolha de títulos')
            break
        else:
            for acha_filme in range(len(filmes)):
                if escolha == filmes[acha_filme]['Title']:
                    print('-=' * 20)
                    print('Titulo:', filmes[acha_filme]['Title'])
                    print('Ano:', filmes[acha_filme]['Year'])
                    print('Tipo:', filmes[acha_filme]['Type'])
                    print('Poster:', filmes[acha_filme]['Poster'])
                    print('-=' * 20)
                    print('')
        print('')


while True:
    print('')
    pesquisa = str(input('Escreva o nome do filme que deseja ou |SAIR| para fechar: '))
    if pesquisa in ('sair', 'SAIR'):
        print('Saindo...')
        break
    else:
        filmes = lista_filmes(pesquisa)
        if filmes == []:
            print(f'Filme {pesquisa} não encontrado')
        else:
            printar_quantidade_filmes(filmes)
            printar_titulos_das_lista_de_filmes(filmes)
            deseja_mais_informacao(filmes)
