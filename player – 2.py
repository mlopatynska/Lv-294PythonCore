import pygame

pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and Draw")

#picture
ball=pygame.image.load("5.png")
colorkey=ball.get_at((0,0))
ball.set_colorkey(colorkey)
ball_x=0
ball_y=0
ball_weigh=100
ball_height=100

timer=pygame.time.Clock()

speedx=5
speedy=5

#paddle
paddle_weigh=200
paddle_heigh=25
paddle_x=300
paddle_y=550
paddle_colour=(255,255,255)

lives=5
score=0

#font
font=pygame.font.SysFont("Times",24)

cl=pygame.image.load("9.jpg")

pygame.mixer.init()
pop=pygame.mixer.Sound("pop.wav")

done =True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                lives = 5
                score = 0
                speedx = 5
                speedy = 5
                ball_x = 0
                ball_y = 0
        if event.type == pygame.KEYDOWN: # why?
            if event.type == pygame.K_LEFT:
                paddle_x -= speedx
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                paddle_x += speedx

    ball_x +=speedx
    ball_y +=speedy

    if ball_x <= 0 or ball_x + ball.get_width()>=800:
        speedx=-speedx*1.01

    if ball_y <= 0:
        speedy =- speedy+0.01

    if ball_y >= 500:
        lives -=1
        speedy = - 5
        speedx = 5

    if lives < 0:
        lives = 0


    screen.blit(cl,(0,0))
    screen.blit(ball,(ball_x,ball_y))
    #drawing of paddle
    paddle_x=pygame.mouse.get_pos()[0]
    paddle_x-=paddle_weigh/2
    pygame.draw.rect(screen,paddle_colour,(paddle_x,paddle_y,paddle_weigh,paddle_heigh))

    if ball_y+ball_height >= paddle_y and ball_y+ball_height<=paddle_y+paddle_heigh and speedy >0:
        if ball_x+ball_weigh/2>= paddle_x and ball_x + ball_weigh/2<= paddle_x+paddle_weigh:
            score +=1
            speedy=-speedy
            pop.play()


    draw_string= "Lives "+str(lives)+" Score: "+str(score)
    text = font.render(draw_string,True,(233,123,102))
    text_rect =text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y =10

    if lives==0:
        speedy=0
        speedx=0
        draw_string ="Game over, but you can try one more time. Just press F1"
        text = font.render(draw_string, True, (123, 123, 212))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10

    screen.blit(text,text_rect)

    pygame.display.update()
    timer.tick(60)

pygame.quit()

