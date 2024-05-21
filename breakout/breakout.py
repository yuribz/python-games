import pygame, sys, random
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((600, 400))

bricks = []

paddle = pygame.rect.Rect((100, 325, 200, 25))

ball = None

for i in range(6):
    for j in range(6):
        bricks.append(
            pygame.rect.Rect((j * 100, i * 25, 100, 25))
        )

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for brick in bricks:
        pygame.draw.rect(screen, (255, 255, 255), brick)
        pygame.draw.rect(screen, (0, 0, 0), brick, width = 2)
    
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    pos = pygame.mouse.get_pos()
    if pos[0] <= 400:
        paddle.left = pos[0]
    else:
        paddle.left = 400
    
    pygame.display.update()