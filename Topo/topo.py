import pygame,random
from pygame.sprite import Sprite
from pygame.locals import *

class Topo(Sprite):
    def __init__(self, pos, ubicacion):
        Sprite.__init__(self)
        self.image = pygame.image.load("Topo/imgs/topo.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.ubicacion=ubicacion
    def update(self,mazo,hoyos,puntaje):
        if mazo.rect.colliderect(self.rect) and pygame.mouse.get_pressed()[0]==1:
            sale=random.randrange(9)
            hoyo=hoyos[sale]
            posiMouse=pygame.mouse.get_pos()
            i=0
            while i<4000:
                pygame.mouse.set_pos(posiMouse)
                i+=1
            puntaje+=1
            return (Topo(hoyo.posicion,sale),puntaje)
        else:
            return (self,puntaje)

