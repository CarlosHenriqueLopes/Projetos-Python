class cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.opcoes = ['basic', 'premium']
        if plano in self.opcoes:
            self.plano = plano
        else:
            print('Plano invalido')


    def mudar_plano(self, novo_plano):
        if novo_plano in self.opcoes:
            self.plano = novo_plano
        else:
            print('Plano invalido')


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme: {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme: {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(f'Para assisti o filme: {filme}, você precisa ter o plano Premium')



cadastro = cliente('Carlos', 'carlos@email.com', 'basic')
print(cadastro.nome)
print(cadastro.email)
print(cadastro.plano)
print()
# Filme plano Premium
cadastro.ver_filme('Batman versão do diretor', 'premium')

# Filme plano basic Basic
cadastro.ver_filme('Batman', 'basic')

# Atribuindo um novo valor ao plano usando .mudar_plano()
cadastro.mudar_plano('premium')

# Conferindo plano
print(cadastro.plano)

# Filme versão Premium
cadastro.ver_filme('Batman versão do diretor', 'premium')

