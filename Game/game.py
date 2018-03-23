import pygame

#static variabel
_WEIGHT = 800
_LENGTH = 600
_PLAY = True
time = pygame.time.Clock()
FPS = 60


class Ball():
    def __init__(self):
        self._size = 10      # size x == size y
        self.start_x = 400
        self.start_y = 150
        self._color = [200, 0, 0]
        self.direction_of_movement = 2
        self.direction_of_movement_x = 4



    def draw(self):
        pygame.draw.circle(screen, self._color,
                           [self.start_x, self.start_y],
                           self._size)

    def check_y(self):
        if self.start_y <= 10:
            self.start_y = 10
            self.direction_of_movement *= -1
        elif self.start_y >= 590:
            self.start_y = 590
            self.direction_of_movement *= 0

    def check_x(self):
        if self.start_x >= 790:
            self.start_x = 790
            self.direction_of_movement_x *= -1
        elif self.start_x <= 10:
            self.start_x = 10
            self.direction_of_movement_x *= -1


    def move(self):
        self.start_x -= self.direction_of_movement_x
        self.start_y -= self.direction_of_movement
        self.check_y()
        self.check_x()



class Line():
    def __init__(self):
        self.length = 10
        self.weight = 50
        self.start_x = 375
        self.start_y = 475
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
    global FPS
    if (t.start_y < ball.start_y + 10 <= t.start_y + 10
        and t.start_x <= ball.start_x <= t.start_x + 50):
        ball.start_y = t.start_y - 10
        ball.direction_of_movement *= -1
        points += 100
    if 0 <= points <= 1000:
        FPS = 60 + points//10




while _PLAY:
    time.tick(FPS)
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
    ball.move()
    check()
    ball.draw()
    t.draw()
    if ball.direction_of_movement == 0:
        _PLAY = False
    pygame.display.flip()


pygame.quit()
