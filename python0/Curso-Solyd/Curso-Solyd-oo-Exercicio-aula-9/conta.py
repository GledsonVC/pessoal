class Conta():

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if valor > self.saldo + self.limite:
            print(f'Saque excede o limite de sua conta')
            self.consulta_saldo()
        else:
            self.saldo -= valor

    def depositar(self, valor):
        valor_deposito = self.saldo
        if valor > 0:
            self.saldo += valor
            print(f'Deposito concluido de {valor_deposito}')
        else:
            print('Problema com o depósito')

    def consulta_saldo(self):
        saldo_mais_limite = self.saldo + self.limite
        print(f'Saldo: {round(self.saldo, 2)} // Saldo+Limite: {round(saldo_mais_limite, 2)}')
