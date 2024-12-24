class Cadastro:
  def __init__(self, nome):
    self.nome = nome
  
  def novo(self):
    arquivo = open('arquivo.txt', 'a')
    arquivo.write((str(self.nome).title()) + '\n')
    print('Cadastro efetuado')