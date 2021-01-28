import pygame
import random
pygame.init()
winWidth = 640
winHeight = 480
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface(win.get_size())
ballSurface = pygame.Surface((50, 50))
ballSurface.set_colorkey((0, 0, 0))
pygame.draw.circle(ballSurface, (255, 180, 34), (25, 25), 10)
bg.fill((255, 255, 255))
win.blit(ballSurface, (100, 100))
pygame.draw.rect(bg, (45, 100, 34), (200, 200, 50, 80))
pygame.draw.arc(bg, (56, 105, 240), (300, 300, 80, 50), 3.14, 6.28)
pygame.draw.polygon(bg, (120, 120, 120), [(20, 30), (100, 100), (50, 150)])
win.blit(bg, (0, 0))
win.blit(ballSurface, (40, 240))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    pygame.display.update()
pygame.quit()
