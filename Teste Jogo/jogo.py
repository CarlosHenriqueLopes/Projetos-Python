

from cgitb import grey
import pygame
pygame.init()

#Para definir o tamanho da janela
janela = pygame.display.set_mode((800, 600))
# -> Para adicionar um nome em cima da janela
pygame.display.set_caption('Jogo da bolinha com Python')

# para manter a janela aberta até que o usuario a feche
jaela_aberta = True
while jaela_aberta:
    pygame.time.delay(50) #mile segundos
    for c in pygame.event.get():
        if c.type == pygame.QUIT:
            jaela_aberta = False

    pygame.draw.circle(janela, color=(0,200,210))
    pygame.display.update()
pygame.quit()