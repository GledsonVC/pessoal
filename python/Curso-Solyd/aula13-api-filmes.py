import requests
import json

req = None


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=7bb6880e')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None


def printar_detalhes(filme):
    print('Título: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Atores: ', filme['Actors'])
    print('Nota: ', filme['imdbRating'])
    print('Ganhos', filme['Awards'])
    print('Capa: ', filme['Poster'])
    print('')


while True:
    op = str(input('Escreva o nome de um filme ou SAIR para fechar: ').upper())
    if op == 'SAIR':
        print('Saindo...')
        break
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print(f'Filme {op} não encontrado ')
        else:
            printar_detalhes(filme)
