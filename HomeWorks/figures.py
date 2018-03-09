import pygame
from random import randint
from random import shuffle
import time
pygame.init()

size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Random figures")

clock = pygame.time.Clock()


class Figure():
    def __init__(self):
        self.x = randint(100, 700)
        self.y = randint(100, 700)
        self.radius = randint(1, 400)
        self.width = randint(1, 400)
        self.heigh = randint(1, 400)
        self.color = [randint(0, 255) for i in range(3)]
        self.side1=[randint(0, 1000) for i in range(2)]
        self.side2 = [randint(0, 1000) for i in range(2)]
        self.side3 = [randint(0, 1000) for i in range(2)]


class Circle(Figure):
    def paint(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Rect(Figure):
    def paint(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigh))


class Polygon(Figure):
    def paint(self):
        pointlist = [self.side1, self.side2, self.side3]
        pygame.draw.polygon(screen, self.color, pointlist)


class Elipse(Figure):
    def paint(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.heigh))


figures_list = []
# for i in range(500):
#     staff1 = Circle()
#     figures_list.append(staff1)
# for d in range(500):
#      staff2 = Elipse()
#      figures_list.append(staff2)
# for b in range(500):
#      staff3 = Rect()
#      figures_list.append(staff3)
# for n in range(500):
#     staff4 = Polygon()
#     figures_list.append(staff4)

for i in range(500):
    figures_list.append(Circle())
    figures_list.append(Elipse())
    figures_list.append(Rect())
    figures_list.append(Polygon())

shuffle(figures_list)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((44,79,39))

    for i in figures_list:
        i.paint()
        #time.sleep(0.5)


    pygame.display.flip()

    clock.tick(10)

pygame.quit()
quit()
