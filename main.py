import pygame
from pygame.locals import *
import random

pygame.init()

class DrawInformation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BirdPlane")

        BLACK = 0, 0, 0
        RED = 255, 0, 0
        YELLOW = 255, 255, 0

def main():
    run = True
    clock = pygame.time.Clock()
    draw_info = DrawInformation(1600, 800)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()