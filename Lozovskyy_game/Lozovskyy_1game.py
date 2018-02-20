import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Lozovskyy's_games")
clock = pygame.time.Clock()
background_image=pygame.image.load ("ocean.jpg")
player_image=pygame.image.load ("fish.jpg")

WHITE =(255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
i = 0

done = False
Rect_stop = False

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
            Rect_stop = not Rect_stop
        elif event.type == pygame.MOUSEMOTION:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]

        # print(event)
    # screen.fill (WHITE)
    screen.blit(background_image, [0, 0])
    if not Rect_stop:
        screen.blit(player_image, [x-25, y-70])

    pygame.draw.line(screen, GREEN, [25,0], [100, 500], 7)
    # pygame.draw.line(screen, RED, [99, 500], [301, 500], 7)
    pygame.draw.circle(screen, BLUE, [400,300], 100, 100)

    pygame.draw.rect(screen, BLACK, [i,0, 25,25], 3)

    if not Rect_stop:
        if i > 800:
            i = 0
        else:
            i+=50
    pygame.draw.rect(screen, BLACK, [0, i, 25, 25], 3)

    pygame.display.update()

    clock.tick(60)
pygame.quit()
quit()
