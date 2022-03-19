import sys
import pygame
import random
from colores import dictyonary

# screen size
width_ = 600
high_ = 600

# FPS
FPS = 30

class Margen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trian.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
    def update(self, left_, right_):
        if left_ < 0:
            self.rect.left = 0
        if right_ > width_:
            self.rect.right = width_

class Triangle(pygame.sprite.Sprite):
    # sprite del jugador
    def __init__(self, margen:Margen):
        self.margen_ = margen
        super().__init__()
        self.image = pygame.image.load("trian.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (width_ // 2, 600)
        self.speed_x = 0
        self.speed_y = 0

    # move the triangle
    def update(self):

        self.speed_x = 0
        self.speed_y = 0

        keys = pygame.key.get_pressed()  # teclas pulsadas
        if keys[pygame.K_LEFT]:
            self.speed_x = -6
            # print(self.velocidad_x)
            # print(self.rect.x)
        if keys[pygame.K_RIGHT]:
            self.speed_x = 6
        if keys[pygame.K_UP]:
            self.speed_y = -6
        if keys[pygame.K_DOWN]:
            self.speed_y = 6

        # Shooting

        if keys[pygame.K_SPACE]:
            player__.shooting__()

        # save new position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # margin sides
        left__ = self.rect.left
        right__ = self.rect.right

        self.margen_.update(left__, right__)
        '''
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO'''

        # bottom margin

        if self.rect.bottom > high_:
            self.rect.bottom = high_

        # upper limit
        if self.rect.top < 200:
            self.rect.top = 200

    def shooting__(self):
        bullet_ = Shots(self.rect.centerx, self.rect.top)  # position in the center of the player rectangle
        bullets_sprite.add(bullet_)


class Enemies(pygame.sprite.Sprite):
    # enemy sprite
    def __init__(self):
        super().__init__()
        self.img_random_ = random.randrange(3)
        if self.img_random_ == 0:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (100, 100))
            self.radius = 50
        if self.img_random_ == 1:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (50, 50))
            self.radius = 25
        if self.img_random_ == 2:
            self.image = pygame.transform.scale(pygame.image.load("circu.png").convert(), (25, 25))
            self.radius = 12

        self.image.set_colorkey(dictyonary.get("NEGRO"))
        self.rect = self.image.get_rect()
        #circle position
        self.rect.x = random.randrange(width_ - self.rect.width)  #we subtract width of the rectangle
        self.rect.y = random.randint(0, 150)  #generate the circle

        self.speed__y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed__y
        if self.rect.top > high_:
            self.rect.x = random.randrange(width_ - self.rect.width)
            self.rect.y = random.randint(0, 150)
            self.speed__y = random.randrange(1, 4)


class Shots(pygame.sprite.Sprite):
    #parameters exact position where it generates shots
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("disparo.jpg").convert(), (10, 20))
        self.rect = self.image.get_rect()
        self.rect.bottom = y  # bottom
        self.rect.centerx = x  # center the rectangle in the middle

    def update(self):  # update bullet position
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()


class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recta.png").convert()
        self.rect = self.image.get_rect()  # get rectangle
        self.rect.x = random.randrange(width_ - 50)
        self.rect.y = 550


# Pygame initialization, window creation, title and clock control.
pygame.init()
pantalla = pygame.display.set_mode((width_, high_))
pygame.display.set_caption("Game shoots")
clock = pygame.time.Clock()

margenn = Margen()

#sprite group, object instantiation
enemies_sprite = pygame.sprite.Group()

base_sprite = pygame.sprite.Group()
for indice in range(6):
    base = Base()
    base_sprite.add(base)

for inidice in range(5):
    enemie__ = Enemies()
    enemies_sprite.add(enemie__)

bullets_sprite = pygame.sprite.Group()

player_sprite = pygame.sprite.Group()
player__ = Triangle(margenn)
player_sprite.add(player__)

ejecutando = True
lives_ = 3
bases = 6
while ejecutando:

    # It is what specifies the speed of the game loop
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    player_sprite.update()
    enemies_sprite.update()
    bullets_sprite.update()
    base_sprite.update()

    ship_collision = pygame.sprite.groupcollide(player_sprite, enemies_sprite, False, False)

    bullet_collision = pygame.sprite.groupcollide(enemies_sprite, bullets_sprite, True, True)

    collision_base = pygame.sprite.groupcollide(base_sprite, enemies_sprite, True, False)

    if ship_collision:
        # enemigo.kill()
        lives_ -= 1
        print("ship collision" + str(lives_))
        if lives_ <= 0:
            print("You lose")
            player__.kill()
            sys.exit()
    if bullet_collision:
        print("collision shot")
    if collision_base:
        bases -= 2
        print("collision base " + str(bases))
        if bases <= 0:
            print("they have destroyed your base, you have lost")
            sys.exit()

    # background screen

    pantalla.fill(dictyonary.get("NEGRO"))

    player_sprite.draw(pantalla)
    enemies_sprite.draw(pantalla)
    bullets_sprite.draw(pantalla)
    base_sprite.draw(pantalla)

    pygame.draw.line(pantalla, dictyonary.get("H_50D2FE"), (300, 0), (300, 600), 1)
    pygame.draw.line(pantalla, dictyonary.get("AZUL"), (0, 300), (800, 300), 1)

    pygame.display.flip()

pygame.quit()
