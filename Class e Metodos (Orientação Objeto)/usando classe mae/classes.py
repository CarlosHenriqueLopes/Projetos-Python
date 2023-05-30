class Veiculo():
    def __init__(self, cor, marca, roda, tanque):
        self.cor = cor
        self.marca = marca
        self.roda = roda
        self.tanque = tanque


class Carro():

    # aqui eu chamo os paremetro da classe mae
    def __init__(self, cor, marca, tanque):
        # aqui eu uso as msm caracteristicas, e tb posso definir
        Veiculo.__init__(self, cor, marca, 4, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 120:
            print("Tanque cheio")
        else:
            self.tanque += litros


class Moto():
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, marca, 2, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 80:
            print("Tanque cheio")
        else:
            self.tanque += litros


class Caminhao():
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, marca, 14, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 220:
            print("Tanque cheio")
        else:
            self.tanque += litros