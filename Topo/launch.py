import pygame,sys,random
from pygame.locals import *
from escenario import Hoyo
from topo import Topo
from cursor import Cursor

size = width, height = 626, 626
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    background_image = pygame.image.load("Topo/imgs/escenario2.jpg")
    background_rect = background_image.get_rect()
    posicionIN=(200,500)
    hoyos=[]
    clock = pygame.time.Clock()
    for i in range(1,4):
    	for j in range(1,4):
	    	posicionIN=(120*i,350+j*50)
	    	hoyos.append(Hoyo(posicionIN))
    count=0
    sale=random.randrange(9)
    pygame.mouse.set_visible(0)
    puntaje=0
    while 1:
    	screen.blit(background_image, background_rect)
    	cont=0
        for hoyo in hoyos:
    		screen.blit(hoyo.image,hoyo.rect)
        cont= sale
        hoyo=hoyos[cont]
        if count==0:
            topo=Topo(hoyo.posicion,cont)
            count=100
        screen.blit(topo.image,topo.rect)
        count-=1
        mazo=Cursor()
        posicionMazo=mazo.update()
        (topo,puntaje)=topo.update(mazo,hoyos,puntaje)
        screen.blit(topo.image,topo.rect)
        screen.blit(mazo.image,posicionMazo)
    	for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        anterior=sale
        while sale==anterior :
            sale=random.randrange(9)
        textoSalida="Puntos: "
        textoSalida+=str(puntaje)
        fuente=pygame.font.Font(None,25)
        texto=fuente.render(textoSalida,True,(0,0,0))
        screen.blit(texto,[30,30])
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__': 
    main()
