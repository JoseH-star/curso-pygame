from tkinter import Image
from xml.etree.ElementTree import canonicalize

import pygame
import constantes
from personaje import Personaje
from weapon import Weapon


pygame.init()

#configuracion ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

# este es el titulo del juego
pygame.display.set_caption("Primer Juego")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_width()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#importar imagenes
animaciones = []
for i in range (10):
        img = pygame.image.load(f"assets//images//characters//player//player_{i}.png")
        img = escalar_img(img, constantes.SCALA_PERSONAJE)
        animaciones.append(img)
#arma
imagen_pistola = pygame.image.load(f"assets//images//weapons//gun.png")
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

#crear un jugador de la clase personaje
jugador = Personaje(50,50, animaciones)

#crear una arma de la clase weapon
pistola = Weapon(imagen_pistola)




# movimineto del jugador
mover_Arriba = False
mover_Abajo = False
mover_Derecha = False
mover_Izquierda = False

# controlar el frame rame
reloj = pygame.time.Clock()


run = True
while run == True:

    #que vaya al 60 FPS
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    #calcular el movimineto del jugador
    delta_x = 0
    delta_y = 0


    if mover_Derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_Izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_Arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_Abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    #actualiza estado del jugador
    jugador.update()


    #actualiza estado del arma
    pistola.update(jugador)

    #dibujar el jugador
    jugador.dibujar(ventana)

    #dibujar el arma
    pistola.dibujar(ventana)


    for event in pygame.event.get():
        #para cerrar el juego
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_Izquierda = True
            if event.key == pygame.K_d:
                mover_Derecha = True
            if event.key == pygame.K_s:
                mover_Abajo = True
            if event.key == pygame.K_w:
                mover_Arriba = True

         # Para detener el movimiento cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                    mover_Izquierda = False
            if event.key == pygame.K_d:
                    mover_Derecha = False
            if event.key == pygame.K_s:
                    mover_Abajo = False
            if event.key == pygame.K_w:
                    mover_Arriba = False



    pygame.display.update()


pygame.quit()



