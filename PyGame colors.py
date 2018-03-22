import pygame
from random import randint
pygame.init()


class Rectangle():
    def __init__(self):
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.width = randint(20,150)
        self.height = randint(20,150)
        self.change_x = randint(0,50)
        self.change_y = randint(0,50)
        self.colors=(randint(0,255),randint(0,255),randint(0,255))
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)


class  Circle():
    def __init__(self):
        self.pos = randint(0, 400)
        self.radius = randint(0,400)
        self.change_pos = randint(0,50)
        self.colors=(randint(0,255),randint(0,255),randint(0,255))
    def move1(self):
        self.pos += self.change_pos
    def draw1(self):
        pygame.draw.circle(screen, self.colors, [self.pos,self.pos], self.radius)


class Polygon():
    def __init__(self):
        self.A1 = randint(0, 600)
        self.A2 = randint(0, 600)
        self.B1 = randint(0, 600)
        self.B2 = randint(0, 600)
        self.C1 = randint(0, 600)
        self.C2 = randint(0, 600)
        # self.pos_p = randint(0, 500)
        # self.change_pos_p = randint(-3, 4)
        self.colors = (randint(0,255),randint(0,255),randint(0,255))
    # def move2(self):
    #     self.pos_p += self.change_pos_p
    def draw2(self):
        pygame.draw.polygon(screen, self.colors, [[self.A1, self.A2], [self.B1, self.B2], [self.C1, self.C2]])




screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("PyGame colors")
clock = pygame.time.Clock()
rect_stop=True
done = False
white=(255,255,255)
red=(255,0,0)
green=(0,128,0)
blue=(0,0,225)
black=(0,0,0)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
        elif event.type==pygame.MOUSEMOTION:
            player_position=pygame.mouse.get_pos()
            x=player_position[0]
            y=player_position[1]

    my_list = []
    for ir in range(100):
        my_rect = Rectangle()
        my_list.append(my_rect)


    my_list1 = []
    for ic in range(100):
        my_cir = Circle()
        my_list1.append(my_cir)


    my_list2 = []
    for ip in range(100):
        my_pol = Polygon()
        my_list2.append(my_pol)



    screen.fill(white)


    for er in my_list:
        er.draw()
        # er.move()


    for ec in my_list1:
        ec.draw1()
        # ec.move1()


    for ep in my_list2:
        ep.draw2()
        # ep.move2()



    pygame.display.flip()
    clock.tick(5)



pygame.quit()
quit()