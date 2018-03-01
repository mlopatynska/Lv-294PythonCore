import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


clock = pygame.time.Clock()

background=pygame.image.load("fon.jpg").convert()
bob=pygame.image.load("bob.gif").convert()
bob.set_colorkey(WHITE)
screen.blit(background, [0,0])
click_sound = pygame.mixer.Sound("S.wav")
#screen.blit(bob, [300,0])

x_speed = 0
y_speed = 0


x_coord = 350
y_coord = 0

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			click_sound.play()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -3
			if event.key == pygame.K_RIGHT:
				x_speed = 3
			if event.key == pygame.K_UP:
				y_speed = -3
			if event.key == pygame.K_DOWN:
				y_speed = 3


		if event.type == pygame.KEYUP:

			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0


		x_coord = x_coord + x_speed
		y_coord = y_coord + y_speed


	player_position = pygame.mouse.get_pos()
	x = player_position[0]
	y = player_position[1]
	screen.blit(bob, [x, y])

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
quit()

