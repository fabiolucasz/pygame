import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Primeiro jogo")
pontos = 0
rect_x = 50
rect_y = 50
blue_rect_x = 50
blue_rect_y = 50

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))
    rect =pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))
    
    if pygame.key.get_pressed()[K_a]:
        rect_x -= 10
    if pygame.key.get_pressed()[K_d]:
        rect_x += 10
    if pygame.key.get_pressed()[K_w]:
        rect_y -= 10
    if pygame.key.get_pressed()[K_s]:
        rect_y += 10

    blue_rect = pygame.draw.rect(screen, (0, 0, 255), (blue_rect_x, blue_rect_y, 50, 50))
    placar = pygame.font.Font(None, 36)
    texto = placar.render("Placar: " + str(pontos), True, (255, 255, 255))
    screen.blit(texto, (10, 10))
    
    if rect.colliderect(blue_rect):
        blue_rect_x = randint(50, 590)
        blue_rect_y = randint(50, 430)
        pontos += 1

    pygame.display.update()
    pygame.time.Clock().tick(60)


