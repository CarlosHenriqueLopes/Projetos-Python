class Veiculo: # -> classe Mãe

    def __init__(self, nome, velocidade_max, KMpor_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.KMpor_litro = KMpor_litro

    def para_str(self):
        print(f"Nome - {self.nome}")
        print(f"Velocidade maxima - {self.velocidade_max}")
        print(f"KM/L - {self.KMpor_litro}")

    def CapacidadeAcentos(self, capacidade): # parametro para ser digitado algo

        print(f"A capacidade maxima de acentos do veiculo {self.nome} é {capacidade}")



#-------------classe filha ----------------------------------

# Herança da classe mãe
class Carro(Veiculo):

    pass # -> para herdar tudo que está na classe mãe



#------------- 2ª classe filha ----------------------------------

class Onibus(Veiculo):

    # Chamo a mesma def, porque é uma classe com herança
    def CapacidadeAcentos(self, cap_de_acentos=70):
        return super().CapacidadeAcentos(cap_de_acentos) #




veiculo = Veiculo("Carro Esportivo", 120, 100)
veiculo.para_str()
print()

carro = Carro("nome_classe_filha(Formula1)", 200, 10)
carro.para_str()
print()

onibus = Onibus("Onibus", 130, 30)
onibus.CapacidadeAcentos()