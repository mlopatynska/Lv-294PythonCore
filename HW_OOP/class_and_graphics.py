import pygame
from random import randint

SIZE = [800,600]
WORK = True

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)


class Rectangle():
    def __init__(self):
        self.x = randint(0,780)
        self.y = randint(0,530)
        self.wight = randint(20,70)
        self.length = randint(20,70)
        self.color = [randint(0,255) for i in xrange(3)]


    def draw(self):
        pygame.draw.rect(screen,self.color,
                         [self.x,self.y,self.wight,self.length])


class Elipse(Rectangle):

    def draw(self):
        pygame.draw.ellipse(screen,self.color,
                            [self.x, self.y, self.wight, self.length])




my_list = []
for i in xrange(500):
    my_object = Rectangle()
    my_list.append(my_object)
for j in xrange(500):
    my_object = Elipse()
    my_list.append(my_object)




while WORK:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                WORK = False
    for i in my_list:
        i.draw()
    pygame.display.flip()



pygame.quit()
quit()
