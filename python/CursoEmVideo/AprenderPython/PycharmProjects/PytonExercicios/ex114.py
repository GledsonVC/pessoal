# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from socket import gethostbyname
import urllib
import urllib.request
try:
    site = 'www.pudim.com.br'
    site1 = urllib.request.urlopen('http://www.google.com.br')
    gethostbyname(site)

except:
    print('O site Pudim não está acessível no momento.')
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')
    print('Consegui acessar o site Google com sucesso')






