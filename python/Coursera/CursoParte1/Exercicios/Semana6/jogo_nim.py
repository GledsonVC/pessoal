#Jogada do Usuário
def usuario_escolhe_jogada(n, m):
    jogadaInvalida = True
    while jogadaInvalida:
        print()
        jogadorTira = int(input('Quantas peças você vai tirar?'))
        if (jogadorTira < 1) or (jogadorTira > m):
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            jogadaInvalida = False
    return jogadorTira

  
#Jogada do computador    
def computador_escolhe_jogada(n, m):
    computadorTira = n
    while computadorTira % (m+1) != 0:
        computadorTira -= 1
    return (n-computadorTira)


def partida():

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()

    #Quem começa
    if n % (m+1) == 0:
        print('Você começa!')
        vezComputador = False
    else:
        print('Computador começa!')
        vezComputador = True

    #loop para ir até o fim das peças no tabuleiro
    while n != 0:
        if vezComputador == False:
            jogadorTira =  usuario_escolhe_jogada(n, m)
            n = n - jogadorTira
            imprime(vezComputador, jogadorTira, n)
            vezComputador = True
        else:
            computadorTira = computador_escolhe_jogada(n, m)
            n = n - computadorTira
            imprime(vezComputador, computadorTira, n)
            vezComputador = False
    print('Fim do jogo! O computador ganhou!')

    

def imprime(computadorJogador, remove, sobra):
    print()
    if computadorJogador:
        if remove == 1:
            print('O computador tirou uma peça')
        else:
            print('O computador tirou', remove, 'peças')
    else:
        if remove == 1:
            print('Você tirou uma peça')
        else:
            print('Você tirou', remove, 'peças')
    if sobra == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    else:
        if sobra!=0:
            print('Agora restam,', sobra, 'peças no tabuleiro.')
    print()
        

#Campeonato chama 3 partidas
def campeonato():
    numeroDePartida = 1
    while numeroDePartida <= 3:
        print()
        print('**** Rodada', numeroDePartida, '****')
        print()
        partida()
        numeroDePartida += 1
    print()
    print('Placar: Você 0 X 3 Computador')
     

#Inicia o jogo
print()
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
validamdoJogo = False
tipoJogo = 0
while validamdoJogo != True:
    if tipoJogo != 1 and tipoJogo != 2:
        print('1 - para jogar uma partida isolada')
        tipoJogo = int(input('2 - para jogar um campeonato '))
        print()
    else:
        validamdoJogo = True
if tipoJogo == 1:
    partida()
else:
    print('Voce escolheu um campeonato!')
    campeonato()
        
