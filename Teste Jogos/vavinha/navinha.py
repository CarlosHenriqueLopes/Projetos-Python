from turtle import Screen
import pygame

#1. iniciar o pygame
pygame.init()

#definir o tamanho da tela
x = 1280
y = 720

#iniciar a janela
janela = pygame.display.set_mode((x, y))

# adicionar um nome a janela
pygame.display.set_caption('Jogo da Navinha')

nave = pygame.image.load('navinha.png').convert_alpha()
nave = pygame.transform.scale(nave, (x, y)) 

rodando = True
while rodando:

    for c in pygame.event.get():
        if c.type == pygame.QUIT:
            rodando = False

    janela.blit(nave, (0, 0))
    
    pygame.display.update()
