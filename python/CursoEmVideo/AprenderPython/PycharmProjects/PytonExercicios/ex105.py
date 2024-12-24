# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(* n, sit = False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = dict()
    print('-'*20)
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n)/len(n)
    if sit == True:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif  turma['média'] >=5:
            turma['situação'] = 'RAZOAVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma


# Programa principal
resp = notas(3.5, 2, 6.5, sit=True)
help(notas)
print(notas.__doc__)
print(resp)
