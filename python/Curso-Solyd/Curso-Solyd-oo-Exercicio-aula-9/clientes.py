class Clientes:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cfp = cpf
        self.idade = idade

    def __str__(self):
        return 'Mome: ' + self.nome + '\nCPF: ' + str(self.cfp) + '\nIdade: ' + str(self.idade)
