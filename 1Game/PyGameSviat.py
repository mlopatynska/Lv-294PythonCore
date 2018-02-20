import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
# screen.display.set_caption("My first game")
clock = pygame.time.Clock()
i=0
rect_stop=False
done = False
white=(255,255,255)
red=(255,0,0)
green=(0,128,0)
blue=(0,0,225)
black=(0,0,0)
screen.fill(green)
pygame.display.update()
background_image=pygame.image.load("first im.jpg")
player_image=pygame.image.load("second im.jpg")

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
        screen.blit(background_image, [0,0])
        if not rect_stop:
            screen.blit(player_image, [x-25,y-70])
        pygame.draw.line(screen, red, [0, 0], [800, 600], 5)
        pygame.draw.circle(screen, white, [400, 300], 100, 6)

        pygame.draw.rect(screen, blue, [1, 0, 100, 100], 0)
        if not rect_stop:
            if i > 800:
                i = 0
            else:
                i += 10

        pygame.display.update()
        clock.tick(60)
pygame.quit()
quit()









