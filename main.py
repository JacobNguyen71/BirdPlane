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

airplane_images = []
for i in range(2):
    airplane_image = pygame.image.load(f'images/player/fly{i}.png').convert_alpha()
    airplane_image = scale_image(airplane_image, 70)
    airplane_images.append(airplane_image)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.image_index = 0
        self.image_angle = 0
    def update(self):
        self.image_index += 1
        if self.image_index >= len(airplane_images):
            self.image_index = 0
        self.image = airplane_images[self.image_index]
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, self.image_angle)
        self.rect.x = self.x
        self.rect.y = self.y

        if pygame.sprite.spritecollide(self, bird_group, True):
            self.lives -= 1

class Bullet(pygame.sprite.Sprite):
    pass

class Bird(pygame.sprite.Sprite):
    pass

player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

player_x = 30
player_y = game_height // 2
player = Player(player_x, player_y)
player_group.add(player)

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[K_UP] and player.rect.top > padding_y:
        player.y -= 2
    elif keys[K_DOWN] and player.rect.bottom < game_height - padding_y:
        player.y += 2

    game_window.blit(bg, (0 - bg_scroll, 0))
    game_window.blit(bg, (game_width - bg_scroll, 0))
    bg_scroll += 1
    if bg_scroll == game_width:
        bg_scroll = 0

    player_group.update()
    player_group.draw(game_window)


    pygame.display.update()
pygame.quit()
