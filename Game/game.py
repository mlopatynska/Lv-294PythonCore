import pygame
import random

#static variabel
_WEIGHT = 1024
_LENGTH = 720
_PLAY = True
_time = pygame.time.Clock()


class Ball():
    def __init__(self):
        self._size = 20      # size x == size y
        self.start_x = 502
        self.start_y = 566
        self._color = [200, 0, 0]
        self.direction_of_movement = 1
        self.left_and_right_corner = self.corner()
        pygame.draw.ellipse(screen, self._color, [self.start_x,self.start_y,self._size,self._size])


    def corner(self):
        return [self.start_x, self.start_y,self.start_x + self._size, self.start_y + self._size]

    def draw(self):
        pygame.draw.ellipse(screen, self._color, [self.start_x, self.start_y, self._size, self._size])


    def move(self):
        self.start_y -= self.direction_of_movement
        if self.start_y <= 0:
            self.start_y = 0
            self.direction_of_movement = 1
        elif self.start_y >= 720:
            self.start_y = 720
            self.direction_of_movement = -1
        self.draw()

pygame.init()
screen = pygame.display.set_mode((_WEIGHT,_LENGTH))
pygame.display.set_caption("My Game")

ball = Ball()
_time.tick(30)
while _PLAY:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _PLAY = False
    pygame.blit(0,0,0)
    ball.move()
    pygame.display.flip()

pygame.quit()
