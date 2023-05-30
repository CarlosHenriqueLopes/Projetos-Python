class controle():
    def __init__(self, cor, tamanho, marca):
        self.cor = cor
        self.tam = tamanho
        self.marc = marca

    def comand_vol(self, vol):
        if vol == '+':
            print('Aumentando o volume...')
        elif vol == '-':
            print('Diminuindo o volume...')

    def trocar_canal(self, trocar):
        if trocar == '>':
            print('Passando canal...')
        elif trocar == '<':
            print('Voltando canal...')

    def mudar_cor(self, m):
        if m != self.cor:
            self.cor = m
            print(self.cor)
        else:
            print(f"O controle já tem a cor {self.cor}")


# Atribuindo valores do init
controle_tv = controle('Preto', '20cm', 'Sony')
print(controle_tv.cor)

print(f'A TV tem o controle remoto da cor {controle_tv.cor} como o tamanho de {controle_tv.tam} da marca {controle_tv.marc}\n')

controle_tv.comand_vol('+')
controle_tv.comand_vol('-')
print()

controle_tv.trocar_canal('>')
controle_tv.trocar_canal('<')

#Trocando a cor do controle
controle_tv.mudar_cor('Branco')
controle_tv.mudar_cor('Branco')
