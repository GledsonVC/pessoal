# Escopo de variável
def funcao():
    n1 = 4      # Variavel local dentro da def
    global n2   # Aqui está usando o mesmo espaço da variavel de fora logo atribuindo valor a global
    n2 = 4
    print(f'n1 dentro vale {n1} e n2 vale {n2}')


n1 = 2    # Variavel global
n2 = 2
print(f'n1 fora vale{n1} e n2 vale {n2}')
funcao()
print(f'Depois da função n2 fora agora é {n2}')