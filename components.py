# -*- coding: utf-8 -*-

import pygame
from random import randint


class Rectangle(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [0, 0, 25, 25])
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, width)
        self.rect.y = randint(0, height)
