from cadastro import Cadastro

while True:
  nome = str(input('Qual nome deseja cadastrar: '))
  cadastrar = Cadastro(nome)
  cadastrar.novo()
  escolha = str(input('Deseja cadastrar outro nome? S|N : ')).upper()
  while escolha[0] not in 'SN':
    print('Opção inválida.\nDeseja cadastrar outro nome?')
    escolha = str(input('|S| para Sim |N| para Não: ')).upper()
  if escolha[0] == 'N':
    break
