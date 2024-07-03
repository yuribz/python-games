import pygame, sys, random

from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Flappy Box")

by = 200
bv = 0

py = 150
px = 400

clock = pygame.time.Clock()

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bv > 0:
        bv = -8
    
    bv += 0.5
    by += bv

    pygame.draw.rect(screen, (255, 255, 255), (50, by, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (px, 0, 75, py))
    pygame.draw.rect(screen, (0, 255, 0), (px, py + 200, 75, 500))

    px -= 4
    if px <= -75:
        px = 400
        py = random.randint(0, 200)

    if (
        pygame.Rect((px, 0, 75, py)).colliderect((50, by, 50, 50))
        or
        pygame.Rect((px, py + 200, 75, 500)).colliderect((50, by, 50, 50))
        or
        by > 350
        or
        by < 0
    ):
        pygame.quit()
        sys.exit()
        

    pygame.display.update()
    clock.tick(60)
    