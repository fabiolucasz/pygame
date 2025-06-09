import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Primeiro jogo")
pontos = 0
placar = pygame.font.Font(None, 36)

game_over = False
game_over_text_title = pygame.font.Font(None, 72)
game_over_text_subtitle = pygame.font.Font(None, 36)

snake_x = 50
snake_y = 50

snake_speed = 10
x_control = snake_speed
y_control = 0


apple_x = 200
apple_y = 50
snake_list = []
initial_size = 5

def increase_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), (x[0], x[1], 20, 20))

def reload_game():
    global snake_x, snake_y, snake_list, initial_size, pontos, game_over
    snake_x = 50
    snake_y = 50
    snake_list = []
    initial_size = 5
    pontos = 0
    game_over = False
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == snake_speed:
                    continue
                else:
                    x_control = -snake_speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -snake_speed:
                    continue
                else:
                    x_control = snake_speed
                    y_control = 0
            if event.key == K_w:
                if y_control == snake_speed:
                    continue
                else:
                    x_control = 0
                    y_control = -snake_speed
            if event.key == K_s:
                if y_control == -snake_speed:
                    continue
                else:
                    x_control = 0
                    y_control = snake_speed
    
    screen.fill((255, 255, 255))
    snake =pygame.draw.rect(screen, (0, 255, 0), (snake_x, snake_y, 20, 20))
    apple = pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 20, 20))
    
   

    snake_x += x_control
    snake_y += y_control

    texto = placar.render("Pontos: " + str(pontos), True, (0, 0, 0))
    screen.blit(texto, (10, 10))

    if snake.colliderect(apple):
        apple_x = randint(50, 590)
        apple_y = randint(50, 430)
        pontos += 1
        initial_size += 1

    head_list = []
    head_list.append(snake_x)
    head_list.append(snake_y)
    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        game_over = True
        while game_over:
            screen.fill((255, 255, 255))
            game_over_title = game_over_text_title.render("Game Over", True, (255, 0, 0))
            game_over_subtitle = game_over_text_subtitle.render("Pressione R para recomeçar", True, (255, 0, 0))

            screen.blit(game_over_title, (200, 200))
            screen.blit(game_over_subtitle, (200, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reload_game()

    

    if len(snake_list) > initial_size:
        del snake_list[0]
    increase_snake(snake_list)

    pygame.display.update()
    pygame.time.Clock().tick(30)