import os,pygame,sys
from pygame.locals import *

def main():
	pygame.init()
	screen=pygame.display.set_mode((440,310))
	pygame.mouse.set_visible(0)
	background_image = pygame.image.load("imgs/fondo.png")
	background_rect = background_image.get_rect()
	juego1_image=pygame.image.load("imgs/juego1.png")
	juego1_rect= juego1_image.get_rect()
	juego1_rect.move_ip(30,30)
	juego2_image=pygame.image.load("imgs/juego2.png")
	juego2_rect= juego2_image.get_rect()
	juego2_rect.move_ip(300,30)
	puntero_image=pygame.image.load("imgs/puntero2.png")
	puntero_rect=puntero_image.get_rect()
	puntero_rect.top=pygame.mouse.get_pos()[1]-32
	puntero_rect.left=pygame.mouse.get_pos()[0]-32
	textoSalida1="Fabian Esteban Pena Castillo, 20141020051"
	textoSalida2="Duvan Humberto Prieto Suarez, 20132020067"
	fuente=pygame.font.Font(None,25)
	while True:
		screen.blit(background_image, background_rect)
		screen.blit(juego1_image, juego1_rect)
		screen.blit(juego2_image, juego2_rect)
		screen.blit(puntero_image,puntero_rect)
		texto=fuente.render(textoSalida1,True,(0,0,0))
		screen.blit(texto,[30,250])
		texto=fuente.render(textoSalida2,True,(0,0,0))
		screen.blit(texto,[30,265])
		update(puntero_rect,juego1_rect,juego2_rect,screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		puntero_rect.top=pygame.mouse.get_pos()[1]-32
		puntero_rect.left=pygame.mouse.get_pos()[0]-32
		pygame.display.update()
		pygame.time.delay(10)


def update(puntero,juego1,juego2,screen):
	if puntero.colliderect(juego1) and pygame.mouse.get_pressed()[0]==1:
		os.system("python Fate_Go_go/Fate_Go_go.py")
	if puntero.colliderect(juego2) and pygame.mouse.get_pressed()[0]==1:
		os.system("python Topo/launch.py")

if __name__ == '__main__': 
    main()
