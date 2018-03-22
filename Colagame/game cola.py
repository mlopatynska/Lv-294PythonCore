import pygame
import sys
import time

from random import randint

pygame.init()

font = pygame.font.Font(None, 25)


screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("MyGameBear")
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 225)
black = (0, 0, 0)
running = True

class Tara():

    def __init__(self):

        self.image_tara = pygame.image.load("Bus.png")
        self.x2 = 0
        self.y2 = 536

    def Tara_move(self):

        key = pygame.key.get_pressed()
        dist = 15
        if key[pygame.K_RIGHT]:
            self.x2 += dist
            if self.x2 > 464:
                self.x2 = 464
        elif key[pygame.K_LEFT]:
            self.x2 -= dist
            if self.x2 < -1:
                self.x2 = 0

    def draw(self, surface):
        surface.blit(self.image_tara, (self.x2, self.y2))


class Beer(Tara):
    life = 3
    points=0
    def __init__(self):
        self.image_1715 = pygame.image.load("Cola.png")
        self.image_life = pygame.image.load("colaoval2.png")
        self.image_life1 = pygame.image.load("circle3.png")
        self.image_life2 = pygame.image.load("circle2.png")
        self.image_win=pygame.image.load("youwin.png")
        self.image_over = pygame.image.load("gameover.png")
        self.sound=pygame.mixer.Sound("banka.wav")
        self.sound1 = pygame.mixer.Sound("banka1.wav")
        self.sound_win=pygame.mixer.Sound("winsong.wav")
        self.sound_gameover=pygame.mixer.Sound("gameoversong.wav")
        self.x1 = randint(0, 590)
        self.y1 = randint(-1000, -1)
        self.change_x = 0
        self.change_y = 4
        self.x2 = tara.x2
        self.y2 = tara.y2


    def move(self):

        self.x1 += self.change_x
        self.y1 += self.change_y

    def draw1(self):
        screen.blit(self.image_1715, [self.x1, self.y1])
        if (self.y1 > 600):
            self.x1 = randint(0, 590)
            self.y1 = 0
            self.y1 += 1
            Beer.life -= 1
            self.sound1.play()


    def dolly(self, x2, y2):

        self.x2 = x2
        self.y2 = y2
        if (self.y1 + 24 >= self.y2) and (self.x2 - 12 <= self.x1 <= self.x2 + 139):
            self.y1 = randint(-1000, -1)
            Beer.points+=1
            self.sound.play()
        if Beer.points==50:
            self.change_y=5
        if Beer.points==150:
            self.change_y=6
        if Beer.points==300:
            self.change_y=7
        if Beer.points==600:
            self.change_y=8
        if Beer.points==1000:
            self.sound_win.play()
            return screen.blit(self.image_win,[80,50])

    def draw_life(self):

        screen.blit(self.image_life, [514, 25])

    def draw_life1(self):

        if Beer.life==2 :
            return screen.blit(self.image_life1, [521, 54])
        if Beer.life==1:
            return screen.blit(self.image_life2, [521, 54])
        if Beer.life==0:
            self.sound_gameover.play()
            return screen.blit(self.image_over,[80,100])

tara = Tara()
b = Beer()

my_list = []
for i in range(5):
    my_object = Beer()
    my_list.append(my_object)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
    screen.fill(white)
    tara.draw(screen)
    tara.Tara_move()

    text = font.render("{}".format(Beer.points), True, [0, 0, 0])
    screen.blit(text, (533, 37))
    for el in my_list:
        el.draw1()
        el.move()
        el.dolly(tara.x2, tara.y2)
        el.draw_life()
        el.draw_life1()
        if not Beer.life: running = False
        if Beer.points==1000: running = False
    pygame.display.update()
    clock.tick(60)
time.sleep(10)
pygame.quit()
quit()