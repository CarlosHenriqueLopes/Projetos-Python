class carro():
    def __init__(self, marca, cor, modelo, preço):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.preço = preço


    def on_off_carro(self, on_off):
        if on_off in 'on':
            print('Ligando carro...')
        elif on_off in 'off':
            print('Desligando carro...')


    def caracteristicas(self):
        print(
            self.marca,
            self.cor,
            self.modelo,
            self.preço
            )


    def mudar_marca(self, trocar):
        if trocar != self.marca:
            self.marca = trocar


    def mudar_cor(self, trocar):
        if trocar != self.cor:
            self.cor = trocar


    def mudar_modelo(self, trocar):
        if trocar != self.modelo:
            self.modelo = trocar


    def mudar_preço(self, trocar):
        if trocar != self.preço:
            self.preço = trocar



carro = carro('Ford', 'Preto', 'Esportivo', 'R$30,00.00')
print(carro.marca)
print(carro.cor)
print(carro.modelo)
print(carro.preço)
print()

carro.on_off_carro('on')
carro.on_off_carro('off')
print()

carro.caracteristicas()
print()
print()


# Mudando todas as caracteeristicas
carro.mudar_marca('volkswagen')
print(carro.marca)

carro.mudar_cor('Branco')
print(carro.cor)

carro.mudar_modelo('SUV')
print(carro.modelo)

carro.mudar_preço('R$120,000.00')
print(carro.preço)
print()

carro.caracteristicas()