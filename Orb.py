import pygame
import random
from Constants import *

class Orb():
    def __init__(self, window, orb_type):
        self.window = window
        self.orb_type = orb_type
        self.x = random.randint(0, WINDOW_WIDTH - 50)
        self.y = 0
        if orb_type == ORB_TYPE_SPEED:
            self.image = pygame.image.load('images/Speed.png')
        elif orb_type == ORB_TYPE_SHIELD:
            self.image = pygame.image.load('images/Shield.png')
        elif orb_type == ORB_TYPE_SLOW:
            self.image = pygame.image.load('images/SlowMotion.png')
        else:
            raise ValueError("Unknown orb type: " + orb_type)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.y += 5
        self.rect.y = self.y
        return self.y > WINDOW_HEIGHT

    def draw(self):
        self.window.blit(self.image, self.rect)

    def collide(self, playerRect):
        return self.rect.colliderect(playerRect)
