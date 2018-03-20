import pygame
import random

#static variabel
_WEIGHT = 800
_LENGTH = 600
_PLAY = True
time = pygame.time.Clock()


class Ball():
    def __init__(self):
        self._size = 10      # size x == size y
        self.start_x = _WEIGHT // 2
        self.start_y = (_LENGTH - _LENGTH*20//100) + self._size//2
        self._color = [200, 0, 0]
        self.direction_of_movement = -2
        self.direction_of_movement_x = 4



    def corner(self):
        self.left_and_right_corner = [self.start_x, self.start_y,
                                      self.start_x + self._size,
                                      self.start_y + self._size]

    def draw(self):
        pygame.draw.circle(screen, self._color,
                           [self.start_x, self.start_y],
                           self._size)

    def check_y(self):
        if self.start_y <= 0:
            self.start_y = 0
            self.direction_of_movement *= -1
        elif self.start_y >= 600:
            self.start_y = 600
            self.direction_of_movement *= 0

    def check_x(self):
        if self.start_x >= 800:
            self.start_x = 800
            self.direction_of_movement_x *= -1
        elif self.start_x <= 0:
            self.start_x = 0
            self.direction_of_movement_x *= -1


    def move(self):
        self.start_x -= self.direction_of_movement_x
        self.start_y -= self.direction_of_movement
        self.check_y()
        self.check_x()
        self.corner()
        #self.draw()


class Line():
    def __init__(self):
        self.length = 10
        self.weight =  50
        self.start_x = _WEIGHT // 2 - self.weight//2
        self.start_y = (_LENGTH - _LENGTH*20//100) + self.length//2
        self.color = [0,0,200]

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         [self.start_x, self.start_y,self.weight, self.length,])

    def moving_left(self):
        self.start_x -= 5
        if self.start_x <= 0:
            self.start_x = 0


    def moving_right(self):
        self.start_x += 5
        if self.start_x >= 750:
            self.start_x = 750



pygame.init()
screen = pygame.display.set_mode((_WEIGHT,_LENGTH))
pygame.display.set_caption("My Game")

ball = Ball()
t = Line()


draw_point = pygame.font.Font(None,25)

points = 0
move_left = False
move_right = False


def check():
    global points
    if (t.start_y <= ball.start_y + 5 <= t.start_y + 10
        and t.start_x <= ball.start_x <= t.start_x + 50):
        ball.start_y = t.start_y
        ball.direction_of_movement *= -1
        points += 100

while _PLAY:
    time.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _PLAY = False
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    screen.fill([255,255,255])
    text = draw_point.render("Point:{}".format(points),True, [0,0,0])
    screen.blit(text,[0,0])
    if move_left:
        t.moving_left()
    if move_right:
        t.moving_right()
    check()
    ball.move()
    t.draw()
    ball.draw()
    if ball.direction_of_movement == 0:
        _PLAY = False
    pygame.display.flip()


pygame.quit()
