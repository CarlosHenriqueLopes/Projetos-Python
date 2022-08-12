import pygame
from random import randint

pygame.init()

x = 600
y = 600
cima = 0
direita = 1
baixo = 2
esquerda = 3

janela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Jogoda da Cobrinha')
cobrinha = [(200, 200), (210, 200), (220, 200)]

skin = pygame.Surface((10, 10))
skin.fill((200, 100, 200))

maça_posição = (randint(0, 590), randint(0, 590))
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))


rodando = True
while rodando:

    for c in pygame.event.get():
        if c.type == pygame.QUIT:
            rodando = False

    janela.fill((0,0,0))
    janela.blit(maça, maça_posição)
    for pos in cobrinha:
        janela.blit(skin, pos)


    pygame.display.update()