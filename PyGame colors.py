import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PyGame colors")
clock = pygame.time.Clock()
rect_stop=True
done = False
white=(255,255,255)
red=(255,0,0)
green=(0,128,0)
blue=(0,0,225)
black=(0,0,0)

screen.fill(green)
pygame.display.flip()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print(event)



class Rectangle():
    def __init__(self):
        self.x = randint(0, 701)
        self.y = randint(0, 501)
        self.width = randint(20,71)
        self.height = randint(20,71)
        self.change_x = randint(-3,4)
        self.change_y = randint(-3,4)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self):
        print(pygame.draw.rect(screen, green, [self.x, self.y, self.width, self.height], 0))
        pygame.display.update()
        clock.tick()



pygame.quit()
quit()