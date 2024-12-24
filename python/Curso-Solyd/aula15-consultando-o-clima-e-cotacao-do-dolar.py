import re
import requests
import json


def cotacao():
    try:
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        resposta = json.loads(requisicao.text)
        valor = resposta['USDBRL']['bid']
        dolar = re.findall(r'\d+\.\d\d', valor)
        return dolar[0]
    except:
        print('Erro de conexão')


def consulta_clima():
    try:
        requisicao = requests.get('https://api.hgbrasil.com/weather')
        resposta = json.loads(requisicao.text)
        string = \
            'Clima da ' + str(resposta['results']['city']) + '\n' + \
            'Data: ' + str(resposta['results']['date']) + '\n' + \
            'Temperatura: ' + str(resposta['results']['temp']) + 'º\n' + \
            'Descrição do Tempo: ' + str(resposta['results']['description']) + '\n'
        return string
    except:
        print('Erro de conexão')

print('Programa que consulta a cotação do dolar e previsão do tempo. \n Digite 0, 1 ou 2 para:')
while True:
    desejo = ''
    while True:
        desejo = int(input('|0| Sair do programa. \n|1| Cotação do dolar. \n|2| Pevisão do tempo.\n'))
        if desejo not in (0, 1, 2):
            print(f'Opção |{desejo}| inválida ')
        else:
            break
    if desejo == 0:
        break
    elif desejo == 1:
        dolar = cotacao()
        if dolar == None:
            print('Verifique sua internet')
        else:
            print(f'Dolar = {dolar}')
    else:
        clima = consulta_clima()
        if clima == None:
            print('Verifique sua internet')
        else:
            print(f'Clima: {clima}')
    desejo = int(input('Deseja sair digite |0|'))
    if desejo == 0:
        break
    else:
        print('Menu:')

