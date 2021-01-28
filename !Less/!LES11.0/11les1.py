import pygame
import random
pygame.init()
winWidth = 640
winHeight = 480
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface(win.get_size())
bg.fill((255, 255, 255))
ballSurface = pygame.Surface((50, 50))
ballSurface.set_colorkey((0, 0, 0))
pygame.draw.circle(ballSurface, (255, 0, 0), (25, 25), 10)
win.blit(bg, (0, 0))
win.blit(ballSurface, (40, 240))
win.blit(ballSurface, (240, 40))
run = True
t = 0  # pattern
color1 = 0
color2 = 0
fps = pygame.time.Clock()
while run:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    pygame.draw.line(win, (color1, 255-color1, color2), (32*t, 0), (0, 480-24*t))
    pygame.draw.line(win, (255-color2, color2, color1),
                     (32*t, 480), (640, 480-24*t))
    t = t + 1
    if t > 20:
        t = 0
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
    pygame.display.update()
pygame.quit()
