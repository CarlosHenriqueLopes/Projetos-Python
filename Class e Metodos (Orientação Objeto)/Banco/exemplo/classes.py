class Cliente:
    def __init__(self, nome, CPF, idade):
        self.nome = nome
        self.CPF = CPF
        self.idade = idade

    # __str__ usando para mostrar todo o cadastro do __init__, quando for chamado
    def __str__(self):
        return f"Cliente: {self.nome} \nCPF: {self.CPF} \nIdade: {self.idade}"



class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo


    def __str__(self):
        return f"{self.cliente} - Saldo da conta: {self.saldo}"


    def soma(self, dinheiro):
        if dinheiro > 0:
            self.saldo += dinheiro
            print(f"R${dinheiro:.2f} reais foram adicionados a sua conta")
        else:
            print(f"Não è possível adicionar R${dinheiro:.2f} reais")