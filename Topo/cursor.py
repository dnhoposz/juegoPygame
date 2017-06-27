import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Cursor(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("Topo/imgs/maz.png")
        self.rect = self.image.get_rect()
        
    def update(self):
		mouse=pygame.mouse.get_pressed()
		if(mouse[0]==1):
			self.image = pygame.image.load("Topo/imgs/mazGolpea1.png")
			self.rect = self.image.get_rect()
			self.rect.top=pygame.mouse.get_pos()[1]-10
			self.rect.left=pygame.mouse.get_pos()[0]-100
			return pygame.mouse.get_pos()[0]-100,pygame.mouse.get_pos()[1]-10
		else:
			return pygame.mouse.get_pos()[0]-100,pygame.mouse.get_pos()[1]-100
        	
    		
        	