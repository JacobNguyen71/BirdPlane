import pygame
from pygame.locals import *
import random

pygame.init()

game_width = 800
game_height = 500
screen_size = (game_width, game_height)
game_window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("BirdPlane")
padding_y = 50

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

def scale_image(image, new_width):
    image_scale = new_width / image.get_rect().width
    new_height = image.get_rect().height * image_scale
    scaled_size = (new_width, new_height)
    return pygame.transform.scale(image, scaled_size)

bg = pygame.image.load('images/BG.png').convert_alpha()
bg = scale_image(bg, game_width)
bg_scroll = 0
class Player(pygame.sprite.Sprite):
    pass

class Bullet(pygame.sprite.Sprite):
    pass

class Bird(pygame.sprite.Sprite):
    pass

player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    game_window.blit(bg, (0 - bg_scroll, 0))
    game_window.blit(bg, (game_width - bg_scroll, 0))
    bg_scroll += 1
    if bg_scroll == game_width:
        bg_scroll = 0

    pygame.display.update()
pygame.quit()
