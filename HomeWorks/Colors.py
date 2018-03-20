# -*- coding: utf-8 -*-
import pygame
from random import randint

""" Батьківський """

class Rectangle():
    def __init__(self):
        self.x = randint(0, 1000)
        self.y = randint(0, 1000)
        self.height = randint(20, 150)
        self.width = randint(20,150)
        self.change_x = randint(0,100)
        self.change_y = randint(0,100)
        self.colors=(randint(0,255),randint(0,255),randint(0,255))

    """Описуєм зміну"""
    def move_rectangl(self):
        self.x += self.change_x
        self.y += self.change_y

    """Створення"""
    def draw_rectangl(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)

"""Прямокутники"""
class R1(Rectangle):
    def dr_r1(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class R2(Rectangle):
    def dr_r2(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class R3(Rectangle):
    def dr_r3(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class R4(Rectangle):
    def dr_r4(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)
class R5(Rectangle):
    def dr_r5(self):
        pygame.draw.rect(screen, self.colors, [self.x, self.y, self.width, self.height], 0)

""" Круг """

class  Circle(Rectangle):
    def __init__(self):
        self.x = randint(0, 400)
        self.r = randint(0,400)
        self.random_x = randint(0,50)
        self.colors=(randint(0,255),randint(0,255),randint(0,255))
    def move_circle(self):
        self.x += self.random_x
    def draw_circle(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)



class C1(Circle):
    def dr_c1(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)
class C2(Circle):
    def dr_c2(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)
class C3(Circle):
    def dr_c3(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)
class C4(Circle):
    def dr_c4(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)
class C5(Circle):
    def dr_c5(self):
        pygame.draw.circle(screen, self.colors, [self.x,self.x], self.r)


"""Багатокутник"""

class Polygon(Rectangle):
    def __init__(self):
        self.L1 = randint(0, 600)
        self.L2 = randint(0, 600)
        self.L3 = randint(0, 600)
        self.L4 = randint(0, 600)
        self.L5 = randint(0, 600)
        self.L6 = randint(0, 600)
        self.colors = (randint(0,255),randint(0,255),randint(0,255))

    def draw_p(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])


class P1(Polygon):
    def dr_p1(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])
class P2(Polygon):
    def dr_p2(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])
class P3(Polygon):
    def dr_p3(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])
class P4(Polygon):
    def dr_p4(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])
class P5(Polygon):
    def dr_p5(self):
        pygame.draw.polygon(screen, self.colors, [[self.L1, self.L2], [self.L3, self.L4], [self.L5, self.L6]])


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Colors")
clock = pygame.time.Clock()
rectangle_stop=True
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
    r.draw_rectangl()
    r.move_rectangl()

#RECTANGLES

    rect_1=R1()
    rect_1.dr_r1()

    rect_2 = R2()
    rect_2.dr_r2()

    rect_3 = R3()
    rect_3.dr_r3()

    rect_3 = R4()
    rect_3.dr_r4()

    rect_3 = R5()
    rect_3.dr_r5()


    c=Circle()
    c.draw_circle()
    c.move_circle()

    circ_1=C1()
    circ_1.dr_c1()

    circ_2 = C2()
    circ_2.dr_c2()

    circ_3 = C3()
    circ_3.dr_c3()

    circ_4 = C4()
    circ_4.dr_c4()

    circ_5 = C5()
    circ_5.dr_c5()

    p=Polygon()
    p.draw_p()


    poly_1=P1()
    poly_1.dr_p1()

    poly_2 = P2()
    poly_2.dr_p2()

    poly_3 = P3()
    poly_3.dr_p3()

    poly_4 = P4()
    poly_4.dr_p4()

    poly_5 = P5()
    poly_5.dr_p5()



    pygame.display.flip()
    clock.tick(7)




quit()