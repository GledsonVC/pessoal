import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    grauSimilaridade = 0
    for i in range(6):
        grauSimilaridade += abs(as_a[i] - as_b[i])
    
    return abs(grauSimilaridade) / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
##    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    sentenca = separa_sentencas(texto)

    totalFrase = []
    for ind in sentenca:
        totalFrase += separa_frases(ind)

    totalDePalavras = []
    for ind in totalFrase:
        totalDePalavras += separa_palavras(ind)

    totalPalavrasUnica = n_palavras_unicas(totalDePalavras)

    totalPalavrasDiferente = n_palavras_diferentes(totalDePalavras)

    somaTotalPalavra = 0
    for ind in totalDePalavras:
        somaTotalPalavra += len(ind)
    tamMedioPalavra = somaTotalPalavra / len(totalDePalavras)

##    Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase
##    "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato).
##    Nessa frase, a relação Type-Token vale 45=0.8
    relTypeToken = totalPalavrasDiferente / len(totalDePalavras)

##    Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo,
##    na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma
##    vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6
    razaoHapaxLegomana = totalPalavrasUnica / len(totalDePalavras)

##    Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
##    (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    somaCaracterSentenca = 0
    for ind in sentenca:
        somaCaracterSentenca += len(ind)
    tamMedSentenca = somaCaracterSentenca / len(sentenca)

##    Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    compleSenteca = len(totalFrase) / len(sentenca)

##    Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
##    (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
    somaCaracterFrase = 0
    for ind in totalFrase:
        somaCaracterFrase += len(ind)
    tamMedFrase = somaCaracterFrase / len(totalFrase)
    return [tamMedioPalavra, relTypeToken, razaoHapaxLegomana, tamMedSentenca, compleSenteca, tamMedFrase]
    


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com
       maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturaTexto = calcula_assinatura(textos[0])
    grauSimilaridadeTexto = compara_assinatura(assinaturaTexto, ass_cp)
    menorGrau = grauSimilaridadeTexto
    textoInfectado = 1
    for i in range(len(textos)):
        assinaturaTexto = calcula_assinatura(textos[i])
        grauSimilaridadeTexto = compara_assinatura(assinaturaTexto, ass_cp)
        if grauSimilaridadeTexto < menorGrau:
            textoInfectado = i + 1
            menorGrau = grauSimilaridadeTexto
    return textoInfectado
        
    
## Função de para ver se o calcula assinatura está correto
def testaCalcula_assinatura(texto, esperado):
    calculandoAssinatura = calcula_assinatura(texto)
    if calculandoAssinatura == esperado:
        print('Passou no teste!!!')
        print('Valor calculado foi    :', calculandoAssinatura)
        print('E o valor esperado era :', esperado)
    else:
        print('Falhou no teste!!!')
        print('Valor calculado foi    :', calculandoAssinatura)
        print('E o valor esperado era :', esperado)
## chama a função que irá calcular a assinatura, no caso o exemplo comparado a resposta do enunciado    
def exemploAssinatura():
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    esperado = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
    testaCalcula_assinatura(texto, esperado)


assInfectadaTipca =  le_assinatura()
todosTextos = le_textos()
texto  = avalia_textos(todosTextos, assInfectadaTipca)
print('O autor do texto', texto, 'está infectado com COH-PIAH')



    

