import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Hoyo(Sprite):
    def __init__(self, pos):
        Sprite.__init__(self)
        self.posicion=pos
        self.image = pygame.image.load("Topo/imgs/hoyo.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        
    def update(self):
        self.rect = self.rect.move(self.vel)

