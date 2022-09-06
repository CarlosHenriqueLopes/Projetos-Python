class pessoa():
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def comer(self, food):
        if self.comendo: # aqui comendo ainda é False
            print(f'{self.nome} já está comendo')
            
        else:
            print(f'{self.nome} Começou a comer {food}')
            self.comendo = True


    def parar_de_comer(self):
        if not self.comendo: # aqui comendo é False
            print(f'{self.nome} não está comendo, então não pode parar de comer')
        else:
            print(f'{self.nome} parou de comer')
            self.comendo = False


    def falar(self, assunto):
        if self.comendo: # comendo True, para não falar comento
            print(f'{self.nome} não vai falar porque está comendo, pare de comer antes')

        elif self.falando: # aqui falando ainda é False
            print(f'{self.nome} já está falando')

        else:
            print(f'{self.nome} começou a falar sobre {assunto}')
            self.falando = True


    def parar_fala(self):
        if not self.falando: # aqui falando está como True
            print(f'{self.nome} não está falando, então não pode parar de falar')
        else:
            print(f'{self.nome} parou de falar sobre um assunto')
            self.falando = False



pessoa = pessoa('fulano', 20)
print(pessoa.nome)
# comer
pessoa.comer('fruta')
# falar
pessoa.falar('filmes')
# comer denovo
pessoa.comer('fruta')

print()

# parar de comer
pessoa.parar_de_comer()
# falar denovo
pessoa.falar('filmes')
# parar denovo
pessoa.parar_de_comer()

print()

# falar denovo
pessoa.falar('filmes')
# falar denovo
pessoa.falar('musica')

print()

# parar de falar
pessoa.parar_fala()
# parar de falar denovo
pessoa.parar_fala()

pessoa.falar('musica')