import pygame
import random

# Defined color for screen
BLACK = (0, 0, 0)

# Creating main shapes and drawing methods
class Rectangle:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.height = random.randint(30, 90)
        self.width = random.randint(30, 90)
        self.change_x = random.randint(-3, 3)
        if self.change_x == 0:
            self.change_x = 1
        self.change_y = random.randint(-3, 3)
        if self.change_y == 0:
            self.change_y = -1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        self.x = self.x + self.change_x
        self.y = self.y + self.change_y

class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Bubbles Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
my_list = []

#Filling in the list with Rectangle objects
for i in range (0,1000):
    my_object = Rectangle()
    my_list.append(my_object)
# Filling in the list with Ellipse objects
for i in range (0,1000):
    my_object = Ellipse()
    my_list.append(my_object)

# Main Program Loop
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic should go here

    # Screen-clearing code goes here
    screen.fill(BLACK)

    # Drawing code should go here
    for i in my_list:
        i.draw()
        i.move()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()