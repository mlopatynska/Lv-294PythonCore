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


class Rectangle_1(Rectangle):
    def draw_rect1(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class Rectangle_2(Rectangle):
    def draw_rect2(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class Rectangle_3(Rectangle):
    def draw_rect3(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)



class  Circle(Rectangle):
    def __init__(self):
        self.pos = randint(0, 400)
        self.radius = randint(0,400)
        self.change_pos = randint(0,50)
        self.colors=(randint(0,255),randint(0,255),randint(0,255))
    def move1(self):
        self.pos += self.change_pos
    def draw1(self):
        pygame.draw.circle(screen, self.colors, [self.pos,self.pos], self.radius)



class Circle_1(Circle):
    def draw_cir1(self):
        pygame.draw.circle(screen, self.colors, [self.pos,self.pos], self.radius)
class Circle_2(Circle):
    def draw_cir2(self):
        pygame.draw.circle(screen, self.colors, [self.pos,self.pos], self.radius)
class Circle_3(Circle):
    def draw_cir3(self):
        pygame.draw.circle(screen, self.colors, [self.pos,self.pos], self.radius)



class Polygon(Rectangle):
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


class Polygon_1(Polygon):
    def draw_pol1(self):
        pygame.draw.polygon(screen, self.colors, [[self.A1, self.A2], [self.B1, self.B2], [self.C1, self.C2]])
class Polygon_2(Polygon):
    def draw_pol2(self):
        pygame.draw.polygon(screen, self.colors, [[self.A1, self.A2], [self.B1, self.B2], [self.C1, self.C2]])
class Polygon_3(Polygon):
    def draw_pol3(self):
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


    screen.fill(white)
    r=Rectangle()
    r.draw()
    r.move()


    rect_1=Rectangle_1()
    rect_1.draw_rect1()

    rect_2 = Rectangle_2()
    rect_2.draw_rect2()

    rect_3 = Rectangle_3()
    rect_3.draw_rect3()

    c=Circle()
    c.draw1()
    c.move1()

    circ_1=Circle_1()
    circ_1.draw_cir1()

    circ_2 = Circle_2()
    circ_2.draw_cir2()

    circ_3 = Circle_3()
    circ_3.draw_cir3()


    p=Polygon()
    p.draw2()
    # p.move2()

    poly_1=Polygon_1()
    poly_1.draw_pol1()

    poly_2 = Polygon_2()
    poly_2.draw_pol2()

    poly_3 = Polygon_3()
    poly_3.draw_pol3()



    pygame.display.flip()
    clock.tick(0.1)



pygame.quit()
quit()





