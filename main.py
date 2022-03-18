import sys

import pygame
import random
#Tamaño de pantalla
ANCHO = 600
ALTO = 600

#FPS
FPS = 30

# Paleta de colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE= (0,255,0)
AZUL = (0,0,255)
H_50D2FE = (94,210,254)
AMARILLO = (255, 255,0)

class Triangulo(pygame.sprite.Sprite):
    #sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        # self.image = pygame.Surface((200, 200)) #dibujar un cuadrado en la superficie
        self.image = pygame.image.load("trian.png").convert()
        #self.image.set_colorkey(colorcroma)
        #self.image.fill(H_FA2F2F) #el sprite se queda color rojo
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (ANCHO // 2, 600)
        #velocidad del personaje  (inicial)
        self.velocidad_x = 0
        self.velocidad_y = 0

# mover el rectangulo
    def update(self):
        # Actualiza esto cada vuelta de bucle.
        #self.rect.y -= 5
        #if self.rect.bottom < 0: #cuando top sea mayor que alto
        #    self.rect.top = ALTO # poner rect arriba nuevamente

        # velocidad predeterminada cada vuelta del bucle
        self.velocidad_x = 0
        self.velocidad_y = 0

        teclas = pygame.key.get_pressed() #teclas pulsadas
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -6
            #print(self.velocidad_x)
            #print(self.rect.x)
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 6
        if teclas[pygame.K_UP]:
            self.velocidad_y = -6
        if teclas[pygame.K_DOWN]:
            self.velocidad_y = 6

        #disparo

        if teclas[pygame.K_SPACE]:
            jugador.disparo()


        #guardar nueva posicion
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #margen lados
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        #margen abajo
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        #limite superior
        if self.rect.top < 200:
            self.rect.top = 200

    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top) #posición en centro del rectangulo jugador
        balas_sprite.add(bala)


class Enemigos(pygame.sprite.Sprite):
    #sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.img_aleatroria = random.randrange(3)
        if self.img_aleatroria == 0:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (100, 100))
            self.radius = 50
        if self.img_aleatroria == 1:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (50, 50))
            self.radius = 25
        if self.img_aleatroria == 2:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (25, 25))
            self.radius = 12
        #self.rect.y = 5
        # Rectángulo (jugador)
        # self.image = pygame.Surface((200, 200)) #dibujar un cuadrado en la superficie
        #self.image = pygame.image.load("circu.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        #posicion circulo
        self.rect.x = random.randrange(ANCHO - self.rect.width) #restamos ancho del rectangulo
        self.rect.y = random.randint(0, 150) #generar el circulo

        #self.velocidad_x = random.randrange(1, 4)
        self.velocidad_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randint(0, 150)
            self.velocidad_y = random.randrange(1, 4)


class Disparos(pygame.sprite.Sprite):
    #parametros posicion exacta donde genera disparos
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("disparo.jpg").convert(),(10, 20))
        self.rect = self.image.get_rect()  #obtener rectangulo
        self.rect.bottom = y #parte baja
        self.rect.centerx = x #centrar en medio rectangulo

    def update(self): #actualizar posición bala
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()

class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recta.png").convert()
        self.rect = self.image.get_rect()  # obtener rectangulo
        self.rect.x = random.randrange(ANCHO-50)
        self.rect.y = 550



# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Disparos")
clock = pygame.time.Clock()

#grupo de sprites, instanciación de objetos
enemigos_sprite = pygame.sprite.Group()

base_sprite = pygame.sprite.Group()
for indice in range(6):
    base = Base()
    base_sprite.add(base)

for inidice in range(5):
    enemigo = Enemigos()
    enemigos_sprite.add(enemigo)

balas_sprite = pygame.sprite.Group()

jugador_sprite = pygame.sprite.Group()
jugador = Triangulo()
jugador_sprite.add(jugador)

ejecutando = True
vidas = 3
bases = 6
while ejecutando:

    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    jugador_sprite.update()
    enemigos_sprite.update()
    balas_sprite.update()
    base_sprite.update()

    #objeto jugador, gropo del sprite
    colision_nave = pygame.sprite.groupcollide(jugador_sprite, enemigos_sprite, False, False)

    colision_disparo = pygame.sprite.groupcollide(enemigos_sprite, balas_sprite, True, True)

    colisio_base = pygame.sprite.groupcollide(base_sprite, enemigos_sprite, True, False)

    if colision_nave:
        #enemigo.kill()
        vidas -=1
        print("colision de la nave "+ str(vidas))
        if vidas <= 0:
            print("haz perdido")
            jugador.kill()
            sys.exit()
    if colision_disparo:
        print("colision disparo ")
    if colisio_base:
        bases -=2
        print("colision base " + str(bases))
        if bases <=0:
            print("han destruido tu base, haz perdido")
            sys.exit()



    #fondo de pantalla
    pantalla.fill(NEGRO)

    jugador_sprite.draw(pantalla)
    enemigos_sprite.draw(pantalla)
    balas_sprite.draw(pantalla)
    base_sprite.draw(pantalla)
    # lineas de la pantalla
    pygame.draw.line(pantalla, H_50D2FE, (300, 0), (300, 600), 1)
    pygame.draw.line(pantalla, AZUL, (0, 300), (800, 300), 1)
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()
