try: # Operação do sistema
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__}')
#     RetornoSeErro: O problema encontrado foi <class 'ValueError'>
# tbm pode ser outros erros : O problema encontrado foi <class 'ZeroDivisionError'


# esse já trata se tiver um tipo de Valor incorreto ou tIpo incorreto
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')

# Esse se usar um denominador 0 afinal nada é divisivel por zero
except ZeroDivisionError:
    print(f'Não é possível dividir um número por Denominador={b}: ZERO')

# Esse se o sistema for interrompido em algum momento
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

# caso algum outro problema ira mostrar a Causa do erro
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

# Irá aparecer caso tudo de certo sem erros
else:
    print(f'O resultado de {a} dividido por {b} é igual a {r:.1f}')
# Irá fazer independente se der erro ou der tudo certo
finally:
    print('Volte sempre! Muito obrigado')