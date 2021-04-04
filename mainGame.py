import  pygame
from sys import exit

from pygame.locals import *
from gameObjects import *

import  random

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('resources/image/background.png').convert()

plane_img = pygame.image.load('resources/image/shoot.png')

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

bullet_rect = pygame.Rect(1004, 987, 9, 2)
bullet_img = plane_img.subsurface(bullet_rect)

player_down_index = 16
score = 0
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(45)
    screen.fill(0)
    screen.blit(background, (0, 0))

    if not player.is_hit:
        screen.blit(player.image[player.image_index], player.rect)
    else:
        screen.blit(player.image[player.image_index], player_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        key_pressed = pygame.key.get_pressed()
        if not player.is_hit:
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                player.moveLeft()

            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                player.moveRight()

            if key_pressed[K_w] or key_pressed[K_UP]:
                player.moveUp()

            if key_pressed[K_s] or key_pressed[K_DOWN]:
                player.moveDown()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()


