import pygame

#Para iniciar o pygame
pygame.init()

x = 650
y = 650
tela = pygame.display.set_mode((x, y)) # -> para fazer a tela usar .display.set_mmode(())

pygame.display.set_caption('Jogo em Python') # -> para colocar um nome na tela .display.set_caption()

# criando um looping para o jogo
rodando = True
while rodando:
    for c in pygame.event.get(): # loop do evendo da tela
        if c.type == pygame.QUIT:
            rodando = False

    pygame.display.update() # para atualizar a leta a cada looping
#Para sair do pygame

