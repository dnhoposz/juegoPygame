# -*- coding: cp932 -*-
import sys, pygame, random

def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def main():
    Pri = 0
    Vel = 0
    Time = 0
    Dur = 0
    Stop = 0
    Pun = 0
    Aux = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit(0)
        Pantalla.blit(Fondo, (0, 0))
        Pantalla.blit(Ini, (160, 500))
        if Pri == 0:
                if evento.type == pygame.MOUSEBUTTONUP:
                        x , y = evento.pos
                        if x >= 160 and x <= 300:
                                if y >= 500 and y <= 575:
                                        Pri = 1
                                        Stop = 100
                                        Time = 0
                                        Pun = 0
        if Pri == 1:
                if Stop != 0:
                        Stop -= 1
                Pantalla.blit(Fondo2, (0, 0))
                Pantalla.blit(Di, (100, 200))
                Pantalla.blit(Fac, (170, 300))
                if evento.type == pygame.MOUSEBUTTONUP:
                        x , y = evento.pos
                        if x >= 170 and x <= 290:
                                if y >= 300 and y <= 375 and Stop == 0:
                                        Vel = 1750
                                        Dur = 600
                                        Aux = 0
                                        Pri = 2
                Pantalla.blit(Med, (160, 400))
                if evento.type == pygame.MOUSEBUTTONUP:
                        x , y = evento.pos
                        if x >= 160 and x <= 300:
                                if y >= 400 and y <= 475 and Stop == 0:
                                        Vel = 1250
                                        Dur = 400
                                        Aux = 0
                                        Pri = 2
                Pantalla.blit(Dif, (160, 500))
                if evento.type == pygame.MOUSEBUTTONUP:
                        x , y = evento.pos
                        if x >= 160 and x <= 300:
                                if y >= 500 and y <= 575 and Stop == 0:
                                        Vel = 750
                                        Dur = 200
                                        Aux = 0
                                        Pri = 2
        if Dur != 0:
                Time += 1
                while Aux != 0:
                        Aux -= 1
                if Time <= 25:
                        Pantalla.blit(Fate, (0, 0))
                        Pantalla.blit(Puntuacion.render("Tiempo: "+str(Dur), 0, (0, 0, 0)), (0, 0))
                        Pantalla.blit(Puntuacion.render("Puntaje: "+str(Pun), 0, (0, 0, 0)), (0, 30))
                if Time > 25 and Time <= 50:
                        Pantalla.blit(UBW, (0, 0))
                        Pantalla.blit(Puntuacion.render("Tiempo: "+str(Dur), 0, (255, 255, 255)), (0, 0))
                        Pantalla.blit(Puntuacion.render("Puntaje: "+str(Pun), 0, (255, 255, 255)), (0, 30))
                if Time > 50 and Time <= 75:
                        Pantalla.blit(Heavens, (0, 0))
                        Pantalla.blit(Puntuacion.render("Tiempo: "+str(Dur), 0, (255, 255, 255)), (0, 0))
                        Pantalla.blit(Puntuacion.render("Puntaje: "+str(Pun), 0, (255, 255, 255)), (0, 30))
                if Time > 75 and Time <= 100:
                        Pantalla.blit(Ataraxia, (0, 0))
                        Pantalla.blit(Puntuacion.render("Tiempo: "+str(Dur), 0, (255, 255, 255)), (0, 0))
                        Pantalla.blit(Puntuacion.render("Puntaje: "+str(Pun), 0, (255, 255, 255)), (0, 30))
                if Time == 100:
                        Time = 0
                Ram = random.randint(1,18)
                Ramv = random.randint(Vel,Vel+1000)
                Ramx = random.randint(0,5)
                Ramy = random.randint(1,6)
                while Ramv != 0:
                        Ramv -= 1
                        if Ram == 1:
                                Pantalla.blit(Saber, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 3
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 2
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 1
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 2:
                                Pantalla.blit(Shirou, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 3
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 3
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 3
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 3
                        if Ram == 3:
                                Pantalla.blit(Rin, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 2
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 3
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 2
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 4:
                                Pantalla.blit(Archer, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 1
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 3
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 2
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 5:
                                Pantalla.blit(Sakura, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 1
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 1
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 3
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 6:
                                if Time <= 50:
                                        Ram = 5
                                else:
                                        Pantalla.blit(Dark_Sakura, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 5
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 3
                        if Ram == 7:
                                Pantalla.blit(Rider, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 2
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 1
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 3
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 8:
                                Pantalla.blit(Illya, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 3
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 1
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 2
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 9:
                                if Time <= 75:
                                        Pantalla.blit(Kotomine, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        if Time <= 25:
                                                                                Pun += 2
                                                                        if Time > 25 and Time <= 50:
                                                                                Pun += 3
                                                                        if Time > 50 and Time <= 75:
                                                                                Pun += 1
                                else:
                                        Ram = 15
                        if Ram == 10:
                                if Time <= 75:
                                        Pantalla.blit(Gilgamesh, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        if Time <= 25:
                                                                                Pun += 2
                                                                        if Time > 25 and Time <= 50:
                                                                                Pun += 3
                                                                        if Time > 50 and Time <= 75:
                                                                                Pun += 1
                                else:
                                        Ram = 11
                        if Ram == 11:
                                if Time <= 75:
                                        Ram = 10
                                else:
                                        Pantalla.blit(Gil, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        Pun += 5
                        if Ram == 12:
                                if Time <= 75:
                                        Ram = 13
                                else:
                                        Pantalla.blit(Bazett, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 7
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        Pun += 5
                        if Ram == 13:
                                Pantalla.blit(Lancer, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 2
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 2
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 1
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 14:
                                if Time <= 75:
                                        Ram = 6
                                else:
                                        Pantalla.blit(Avenger, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        Pun += 5
                        if Ram == 15:
                                if Time <= 75:
                                        Ram = 3
                                else:
                                        Pantalla.blit(Karen, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        Pun += 5
                        if Ram == 16:
                                if Time <= 75:
                                        Ram = 3
                                else:
                                        Pantalla.blit(Luvia, ((Ramx*70)+15, (Ramy*100)))
                                        if pygame.mouse.get_pressed():
                                                if Aux == 0:
                                                        Aux = 1
                                                        x , y = evento.pos
                                                        if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                                if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                        Pun += 5
                        if Ram == 17:
                                Pantalla.blit(Caster, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 2
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 3
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 1
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                        if Ram == 18:
                                Pantalla.blit(Taiga, ((Ramx*70)+15, (Ramy*100)))
                                if pygame.mouse.get_pressed():
                                        if Aux == 0:
                                                Aux = 1
                                                x , y = evento.pos
                                                if x >= (Ramx*70)+15 and x <= (Ramx*70)+85:
                                                        if y >= (Ramy*100) and y <= (Ramy*100)+100:
                                                                if Time <= 25:
                                                                        Pun += 2
                                                                if Time > 25 and Time <= 50:
                                                                        Pun += 2
                                                                if Time > 50 and Time <= 75:
                                                                        Pun += 2
                                                                if Time > 75 and Time <= 100:
                                                                        Pun += 2
                Dur -=1
        if Dur == 0 and Pun != 0:
                Pantalla.blit(Final, (0, 0))
                Pantalla.blit(Puntuacion.render("Puntaje Final: "+str(Pun), 0, (255, 255, 255)), (150, 300))
                if evento.type == pygame.MOUSEBUTTONUP:
                        Pri = 0
                        Vel = 0
                        Time = 0
                        Dur = 0
                        Stop = 0
                        Pun = 0
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    Pantalla = pygame.display.set_mode((450, 700))
    pygame.display.set_caption("Fate Go Go")
    Fondo = imagen('Fate_Go_Go/Imagenes/Inicio.jpg')
    Fondo2 = imagen('Fate_Go_Go/Imagenes/Dificultad.jpg')
    Fate = imagen('Fate_Go_Go/Imagenes/Fate.jpg')
    UBW = imagen('Fate_Go_Go/Imagenes/Unlimited Blade Works.jpg')
    Heavens = imagen('Fate_Go_Go/Imagenes/Heavens Feel.jpg')
    Ataraxia = imagen('Fate_Go_Go/Imagenes/Ataraxia.jpg')
    Final = imagen('Fate_Go_Go/Imagenes/Final.jpg')
    Fuente = pygame.font.Font(None, 75)
    Puntuacion = pygame.font.Font(None, 30)
    Ini = Fuente.render("Inicio", 0, (0, 0, 0))
    Di = Fuente.render("Dificultad", 0, (0, 0, 0))
    Fac = Fuente.render("Facil", 0, (0, 0, 0))
    Med = Fuente.render("Medio", 0, (0, 0, 0))
    Dif = Fuente.render("Dificil", 0, (0, 0, 0))
    Punt = Puntuacion.render("Puntuacion: ", 0, (0, 0, 0))
    Saber = imagen('Fate_Go_Go/Imagenes/Saber.png')
    Shirou = imagen('Fate_Go_Go/Imagenes/Shirou.png')
    Rin = imagen('Fate_Go_Go/Imagenes/Rin.png')
    Archer = imagen('Fate_Go_Go/Imagenes/Archer.png')
    Sakura = imagen('Fate_Go_Go/Imagenes/Sakura.png')
    Dark_Sakura = imagen('Fate_Go_Go/Imagenes/Dark_Sakura.png')
    Rider = imagen('Fate_Go_Go/Imagenes/Rider.png')
    Illya = imagen('Fate_Go_Go/Imagenes/Illya.png')
    Kotomine = imagen('Fate_Go_Go/Imagenes/Kotomine.png')
    Gilgamesh = imagen('Fate_Go_Go/Imagenes/Gilgamesh.png')
    Gil = imagen('Fate_Go_Go/Imagenes/Gil.png')
    Bazett = imagen('Fate_Go_Go/Imagenes/Bazett.png')
    Lancer = imagen('Fate_Go_Go/Imagenes/Lancer.png')
    Avenger = imagen('Fate_Go_Go/Imagenes/Avenger.png')
    Karen = imagen('Fate_Go_Go/Imagenes/Karen.png')
    Luvia = imagen('Fate_Go_Go/Imagenes/Luvia.png')
    Caster = imagen('Fate_Go_Go/Imagenes/Caster.png')
    Taiga = imagen('Fate_Go_Go/Imagenes/Taiga.png')
    main()
