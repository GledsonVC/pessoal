time = 'Íbis'

print(time[0])
print(time[1])
print(time[2])
print(time[3])


print(time.upper()) ## Todas maiúsculas
print(time.lower()) ## Todas minúsculas

texto = 'ana gosta de banana'
print(texto)
print(texto.capitalize()) ## Primeira letra fica maiúscula

removeEspaçoEmBranco  = '       removendo@inico.fim       '
print(removeEspaçoEmBranco)
print(removeEspaçoEmBranco.strip()) ## Remove no inicio e no fim os espaços em branco

print(texto)
print(texto.count('a')) ## Conta a quantidade de 'a' que contem na variavel

trocaPalavra = 'Eu torço para o Corinthians'
print(trocaPalavra)
print(trocaPalavra.replace('Corinthians', 'São Paulo')) ## Troca palavra existente

## duas função sendo usada uma ja vimos e outra é o centralizador com quantidade de caracter
print(texto.capitalize().center(80))

print(texto.find('de'))  ## retorna a posição do caracter da variavel
print(texto.find('existe'))  ## se não existe ele retorna -1

fruta = 'amora'
print(fruta[:4]) ## pegando parte da variavel str do inicio até 4 lembrando que não pega a ultima
print(fruta[1:]) ## pega do primeiro até o final
print(fruta[2:4]) ## pega da posição 2 até 4 lembrando que a 4 não retorna
