class Cliente:
    def __init__(self, nome, CPF, idade):
        self.nome = nome
        self.CPF = CPF
        self.idade = idade

    # __str__ usando para mostrar todo o cadastro do __init__, quando for chamado
    def __str__(self):
        return f"Cliente: {self.nome} \nCPF: {self.CPF} \nIdade: {self.idade}\n"



class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite


    def consultar_limite(self):
        return f"Seu limite é de: R${self.limite:.2f} reais"


    def aumentar_limite(self, limite):
        self.limite += limite
        return f"R${limite:.2f} reais foi acrescido ao seu limite\n" \
               f"Limite atual: R${self.limite:.2f} reais"


    def soma(self, dinheiro):
        if dinheiro > 0:
            self.saldo += dinheiro
            return f"R${dinheiro:.2f} reais foram adicionados a sua conta\n" \
                   f"Saldo atual: R${self.saldo:.2f} reais"
        else:
            return f"Não è possível adicionar R${dinheiro:.2f} reais ao seu saldo"


    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            return f"R${saque:.2f} reais foram sacados da sua conta"

        # Lógica do elif:
        # se o saque for maior que o saldo atual e saque for maior que a soma do saldo e limite atuais
        # saldo_utilizado recebe o valor do saque menos o saldo, para utilizar ele subtraindo do limite
        # fazendo o com que o saque desconte do limite caso necessário
        elif saque > self.saldo and saque <= (self.saldo + self.limite):
            saldo_utilizado = saque - self.saldo
            self.saldo = 0
            novo_limite = self.limite - saldo_utilizado
            return f"Seu saque foi maior que seu saldo, então foi descontado do seu limite\n" \
                   f"Valor do limite atual: R${novo_limite:.2f}\n" \
                   f"Valor do saldo atual: R${self.saldo:.2f}"

        else:
            return "Não é possível sacar este valor"


    def ver_saldo(self):
        return f"Seu saldo atual é de: R${self.saldo:.2f} reais"