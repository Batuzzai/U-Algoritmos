# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:42:08 2019

@author: chali
"""

from tkinter import *
from tkinter import ttk
import pygame
from pygame.locals import *
import os
import sys


ANCHO = 800
ALTO = 600


class Bala(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bala.png", "", alpha=True)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]
        self.speed = [3, 3]


    def update(self):
        #if self.rect.left < 0 or self.rect.right > ANCHO:
         #   self.speed[0] = -self.speed[0]
        #if self.rect.top < 0 or self.rect.bottom > ALTO:
         #   self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        
    def colision(self,OBJETO):
        self.rect.colliderect(OBJETO.rect)


class Monkey(pygame.sprite.Sprite):
    def __init__(self,HP,AR,DMG,RANGO,posx,posy):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("TTM/ICONO2.png", "", alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        
        self.HP = HP
        self.AR = AR
        self.DMG = DMG
        self.RANGO = RANGO
        self.HPBASE = HP
        self.SCORE = 0
        
    def Limite(self):
        # Controlar que la paleta no salga de la pantalla
        if self.rect.bottom >= ANCHO:
            self.rect.bottom = ALTO
        elif self.rect.top <= 0:
            self.rect.top = 0
            
    def Golpear(self, OBJETO):
        if self.rect.colliderect(OBJETO.rect):
            OBJETO.HP -= self.DMG
            
    def Disparar(self):
        Disparo = Bala()
        Disparo.image = load_image("bala.png", "", alpha=True)
        Disparo.image = pygame.transform.scale(Disparo.image, (10, 10))
        pygame.display.flip()
        Disparo.update()
            
        
        
    
        
    def Cura(self):
        if self.HP <= self.HPBASE:    
            self.HP = self.HPBASE
            
        else:
            self.HP += 50
            
    def Atacar(self,MONO):
        MONO.HP -= self.DMG
        if MONO.HP <= 0:
            self.SCORE += 1
            MONO.HP = MONO.HPBASE
                        
            
            
            
class Jugador():
    def __init__(self,MONO):
        self.MONO = MONO
        self.SCORE = MONO.SCORE

class Partida():
    def __init__(self,MODE,PLAYER1,PLAYER2):
            self.MODE = MODE
            self.TIME = 120 #disminuirá
            self.PLAYER1 = PLAYER1
            self.PLAYER2 = PLAYER2
            


def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print("No se pudo cargar el sonido:", ruta)
        sonido = None
    return sonido
        
            
            
class Juego():
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Brawl Strike: Monkeys Offensive")
    
    fondo = pygame.image.load("mapa.jpg").convert()
    fondo = pygame.transform.scale(fondo, (800, 600))
    
    LUCAPO = Monkey(100,50,50,1,200,ANCHO)
    LUCAPO.image = pygame.transform.scale(LUCAPO.image, (50, 50))
    TUSSI = Monkey(200,0,35,1,ALTO,200)
    TUSSI.image = pygame.transform.scale(TUSSI.image, (50, 50))
    
    LUCAPO.Limite()
    TUSSI.Limite()
    
    LUCAPO.Disparar()
    
    bala = Bala()
    
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 25)
    
    screen.blit(bala.image, bala.rect)
    
    
    screen.blit(fondo, (0, 0))
    
    pygame.display.flip()
    
    while True:
        clock.tick(120)
        bala.update()
        LUCAPO.Disparar()
            
        screen.blit(fondo, (0, 0))
        screen.blit(bala.image, bala.rect)
        screen.blit(LUCAPO.image, LUCAPO.rect)
        screen.blit(TUSSI.image, TUSSI.rect)
        
        pygame.display.flip()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == K_UP:
                    LUCAPO.rect.centery -= 5
                elif event.key == K_DOWN:
                    LUCAPO.rect.centery += 5
                elif event.key == K_LEFT:
                    LUCAPO.rect.centerx -= 5
                elif event.key == K_RIGHT:
                    LUCAPO.rect.centerx += 5
                elif event.key == K_SPACE:
                    LUCAPO.Disparar

                elif event.key == ord('w'):
                    TUSSI.rect.centery -= 5
                elif event.key == ord('s'):
                    TUSSI.rect.centery += 5
                elif event.key == ord('a'):
                    TUSSI.rect.centerx -= 5
                elif event.key == ord('d'):
                    TUSSI.rect.centerx += 5  
                    
                    
                elif event.key == K_ESCAPE:
                    sys.exit(0)
                    
            elif event.type == pygame.KEYUP:
                if event.key == K_UP:
                    LUCAPO.rect.centery += 0
                elif event.key == K_DOWN:
                    LUCAPO.rect.centery += 0
                elif event.key == K_LEFT:
                    LUCAPO.rect.centerx += 0
                elif event.key == K_RIGHT:
                    LUCAPO.rect.centerx += 0
                    
                elif event.key == ord('w'):
                    TUSSI.rect.centery += 0
                elif event.key == ord('s'):
                    TUSSI.rect.centery += 0
                elif event.key == ord('a'):
                    TUSSI.rect.centerx += 0
                elif event.key == ord('d'):
                    TUSSI.rect.centerx += 0
                    
class Aplicacion():

    base = Tk()
    base.geometry('800x600')
    base.configure(bg = 'green')
    base.title("Brawl Strike: Monkeys offensive")
    ttk.Button(base, text='Salir', command=quit).pack(side=BOTTOM)
    ttk.Button(base, text= "Iniciar Juego", command=Juego()).place(x=50,y=50)

    base.mainloop()
       