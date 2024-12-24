import requests

cabecalho = {'User-agent': 'Windows Codigo aberto'}
meus_cookies = {'Ultimavisita': '02-11-2020'}
dados = {'username': 'gledsonvc',
         'password': 'gledson1234'}

texto = None
try:
    requisicao = requests.get('https://putsreq.com/Yx4vUcrhoV1YQ998WwOi',
                              headers = cabecalho,
                              cookies = meus_cookies,
                              data = dados)
    texto = requisicao.text
except Exception as err:
    print('Requisição deu erro: ',e)

print(texto)