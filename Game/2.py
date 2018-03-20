# -*- coding: utf-8 -*-
#
import pygame

"""вікно"""
window = pygame.display.set_mode((600, 630))  # Розширення вікна
pygame.display.set_caption('Sniper')

"""фон"""
screen = pygame.Surface((600, 600))  # Рoзмір фону
background_image=pygame.image.load("fon.png").convert()

"""рядок стану(progressbar)"""
info_string = pygame.Surface((600, 30))

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2):
        return 1
    else:
        return 0

"""шрифти"""
pygame.font.init()
speed_font = pygame.font.Font(None, 32)
inf_font = pygame.font.SysFont('Comic Sans MS', 24, True)
label_font = pygame.font.SysFont('Comic Sans MS', 24, True)

"""опис героя"""
hunter = Sprite(300, 550, "hunter.png")

"""опис цілі"""
target = Sprite(10, 10, "Target.png")
target.right = False
target.step = 1
"""опис ракети"""
rocket = Sprite(450, -10, "rocket.png")
rocket.push = False

done = True
pygame.key.set_repeat (1,1) # дублювання натискання клавіш
enumerator = 0
game_color = 255
while done:
    """оброблення подій"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    """подія - натискання клавіш"""
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
            if hunter.x > 10:
                hunter.x -= 1
        if e.key == pygame.K_RIGHT:
            if hunter.x < 550:
                hunter.x += 1
        if e.key == pygame.K_UP:
            if hunter.y > 300:
                hunter.y -= 1
        if e.key == pygame.K_DOWN:
            if hunter.y < 550:
                hunter.y += 1
        """ запуск ракети"""
        if e.key == pygame.K_SPACE:
            if rocket.push == False:
                rocket.x = hunter.x+30
                rocket.y = hunter.y + 10
                rocket.push = True


    """подія - рух мишки"""
    if e.type == pygame.MOUSEMOTION:
        pygame.mouse.set_visible(False)
        m = pygame.mouse.get_pos()
        if m[0] > 10 and m[0] < 550:
            hunter.x = m[0]
        if m[1] > 300 and m[1] < 550:
            hunter.y = m[1]

    """подія - натискання кнопок мишки"""
    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            if rocket.push == False:
                rocket.x = hunter.x + 30
                rocket.y = hunter.y + 10
                rocket.push = True

    """переміщення героя"""

    """заливка"""
    screen.blit(background_image, [0, 0]) #відображення картинки
    info_string.fill((30, 80, 55))

    """зміна кольору назви гри"""
    game_color += 0.1
    if game_color > 254:
        game_color = 100


    """рух цілі"""
    if target.right == True:
        target.x -= target.step
        if target.x < 0:
            target.right = False
    else:
        target.x += target.step
        if target.x > 560:
            target.right = True

    """переміщення ракети"""
    if rocket.y < 0:
        rocket.push = False
        enumerator -= 1

    if rocket.push == False:
        rocket.x = hunter.x + 30
        rocket.y = hunter.y + 10


    else:
        rocket.y -= 1


    """ попадання ракети в ціль"""

    if Intersect(rocket.x, target.x, rocket.y, target.y, 11, 38) == True:
        rocket.push = False
        target.step += 0.2
        enumerator += 1


    """відображення об'єктів"""
    rocket.render()
    hunter.render()
    target.render()

    """ відображення шрифтів"""
    info_string.blit (speed_font.render (u'Швидкість: '+str(target.step), 1, (50, 200, 200)), (400, 5))
    info_string.blit (inf_font.render(u'Рахунок: '+str(enumerator+1), 1, (50, 200, 200)), (10, 0))
    info_string.blit (label_font.render (u'Стрілок ', 1, (200, game_color, 0)), (240, 0))

    """відображення холста на екран"""

    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 30))
    pygame.display.flip()
    pygame.time.delay(3)
