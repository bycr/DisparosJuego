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
        '''
        if teclas[pygame.K_SPACE]:
            jugador.disparo()
        '''

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

    '''
    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top) #posición en centro del rectangulo jugador
        balas.add(bala)
    '''







# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Disparos")
clock = pygame.time.Clock()

#grupo de sprites, instanciación de objetos
jugador_sprite = pygame.sprite.Group()
jugador = Triangulo()
jugador_sprite.add(jugador)


ejecutando = True
while ejecutando:

    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    jugador_sprite.update()

    #fondo de pantalla
    pantalla.fill(NEGRO)

    jugador_sprite.draw(pantalla)
    # lineas de la pantalla
    pygame.draw.line(pantalla, H_50D2FE, (300, 0), (300, 600), 1)
    pygame.draw.line(pantalla, AZUL, (0, 300), (800, 300), 1)
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()
