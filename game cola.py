import pygame
import os
from random import randint
pygame.init()

class Beer():

    def __init__(self):
        self.image_1715=pygame.image.load("Cola.png")
        self.x = randint(0,600)
        self.y = 0
        self.change_x = 0
        self.change_y = 4


    def move(self):

        self.x+= self.change_x
        self.y+= self.change_y

    def draw(self):
        screen.blit(self.image_1715,[self.x, self.y ])
        # if (self.x > 600):
        #     self.x = 0
        # self.x += 1
        if (self.y > 600):
            self.y = 0
        self.y += 1


# class Beer_1(Beer):
#     def move(self):
#
#         self.x+= self.change_x
#         self.y+= self.change_y

    # def draw(self):
    #     screen.blit(self.image_1715,[self.x, self.y ])
    #     if (self.x > 800):
    #         self.x = 0
    #     self.x += 2
    #     if (self.y > 800):
    #         self.y = 0
    #     self.y += 1



# my_list = []
# for i in range(5):
#     my_object = Beer()
#     my_list.append(my_object)





class Tara():

    def __init__(self):

        self.image_tara = pygame.image.load("Bus.png")
        self.x = 0
        self.y = 536

    def Tara_move(self):

        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        surface.blit(self.image_tara, (self.x, self.y))


# class Score():







screen = pygame.display.set_mode((600, 600))
# b1=Beer_1()
b = Beer()
tara = Tara()
clock = pygame.time.Clock()
pygame.display.set_caption("MyGameBear")
white=(255,255,255)
red=(255,0,0)
green=(0,128,0)
blue=(0,0,225)
black=(0,0,0)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    tara.Tara_move()
    b.move()
    # b1.move()
    screen.fill(white)
    tara.draw(screen)
    b.draw()
    # b1.draw()
    # for i in my_list:
    #     i.draw()
    pygame.display.update()

    clock.tick(60)