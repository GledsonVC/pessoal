try: # Operação do sistema
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except : # Caso algum problema de digitação do usuário que irá dar erro no sistema cai aqui
    print('Tivemos um problema')
else: # Se der tudo certo cai aqui
    print(f'O resultado de {a} dividido por {b} é igual a {r:.1f}')
finally:# Certo ou Errado irá aparecer isso
    print('Volte sempre! Muito obrigado')
