import random, pygame, sys
from pygame.locals import *

fps = 10
window_x = 640
window_y = 480
cell = 20
cells_x = int(window_x / cell)
cells_y = int(window_y / cell)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkgreen = (0, 155, 0)
darkgray = (40, 40, 40)
background = black

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

head = 0 # index of the worm's head

def main():
    global fpsclock, screen, mainfont

    pygame.init()
    fpsclock = pygame.time.Clock()
    screen = pygame.display.set_mode((window_x, window_y))
    mainfont = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Worm')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    startx = random.randint(5, cells_x - 6)
    starty = random.randint(5, cells_y - 6)
    worm_loc = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        if worm_loc[head]['x'] == -1 or worm_loc[head]['x'] == cells_x or \
                worm_loc[head]['y'] == -1 or worm_loc[head]['y'] == cells_y:
            return # gameover
        for wormBody in worm_loc[1:]:
            if wormBody['x'] == worm_loc[head]['x'] and wormBody['y'] == worm_loc[head]['y']:
                return # gameover

        if worm_loc[head]['x'] == apple['x'] and worm_loc[head]['y'] == apple['y']:
            apple = getRandomLocation()
        else:
            del worm_loc[-1]

        if direction == UP:
            new_head = {'x': worm_loc[head]['x'], 'y': worm_loc[head]['y'] - 1}
        elif direction == DOWN:
            new_head = {'x': worm_loc[head]['x'], 'y': worm_loc[head]['y'] + 1}
        elif direction == LEFT:
            new_head = {'x': worm_loc[head]['x'] - 1, 'y': worm_loc[head]['y']}
        elif direction == RIGHT:
            new_head = {'x': worm_loc[head]['x'] + 1, 'y': worm_loc[head]['y']}
        worm_loc.insert(0, new_head)
        screen.fill(background)
        drawGrid()
        drawWorm(worm_loc)
        drawApple(apple)
        drawScore(len(worm_loc) - 3)
        drawSpeed((len(worm_loc) - 3) // 5 + 1)
        pygame.display.update()
        fpsclock.tick(fps + (len(worm_loc) - 3) // 5)


def getRandomLocation():
    return {'x': random.randint(0, cells_x - 1), 'y': random.randint(0, cells_y - 1)}


def drawPressKeyMsg():
    pressKeySurf = mainfont.render('Press any key to play', True, darkgray)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (window_x - 200, window_y - 30)
    screen.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf = titleFont.render('Worm Game', True, white, darkgreen)
    titleRect = titleSurf.get_rect()
    titleRect.center = (window_x / 2, window_y / 2)

    while True:
        screen.fill(background)
        screen.blit(titleSurf, titleRect)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        fpsclock.tick(fps)


def terminate():
    pygame.quit()
    sys.exit()


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, white)
    overSurf = gameOverFont.render('Over', True, white)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (window_x / 2, 10)
    overRect.midtop = (window_x / 2, gameRect.height + 10 + 25)

    screen.blit(gameSurf, gameRect)
    screen.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return

def drawScore(score):
    scoreSurf = mainfont.render('Score: {}'.format(score), True, white)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topright = (window_x - 130, 10)
    screen.blit(scoreSurf, scoreRect)


def drawSpeed(speed):
    scoreSurf = mainfont.render('Speed: {}'.format(speed), True, white)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (window_x - 120, 10)
    screen.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * cell
        y = coord['y'] * cell
        wormSegmentRect = pygame.Rect(x, y, cell, cell)
        pygame.draw.rect(screen, darkgreen, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cell - 8, cell - 8)
        pygame.draw.rect(screen, green, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * cell
    y = coord['y'] * cell
    appleRect = pygame.Rect(x, y, cell, cell)
    pygame.draw.rect(screen, red, appleRect)


def drawGrid():
    for x in range(0, window_x, cell):
        pygame.draw.line(screen, darkgray, (x, 0), (x, window_y))
    for y in range(0, window_y, cell):
        pygame.draw.line(screen, darkgray, (0, y), (window_x, y))


if __name__ == '__main__':
    main()