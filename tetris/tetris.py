import pygame, sys, random
from tetramino import *

from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((10 * 25, 20 * 25))

grid = [[0 for _ in range(10)] for _ in range(20)]

clock = pygame.time.Clock()
timer = 0

t = Tetramino("S")

colors = {
    1: (0, 255, 255), # I
    2: (255, 165, 0), # L
    3: (0, 0, 255),   # J
    4: (0, 255, 0),   # S
    5: (255, 0, 0),   # Z
    6: (128, 0, 128), # T
    7: (255, 255, 0)  # O
}

direction = "down"

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num = grid[i][j]
            if num> 0:
                pygame.draw.rect(screen, colors[num], (j * 25, i * 25, 25, 25))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        direction = "right"

    if timer % 20 == 0:
        
        print(t.shape)
        grid = t.move(grid, direction = direction)
        if t.check_collision(grid = grid, direction = "down"):
            t = Tetramino("Z")
            
        # reset direction only after the move is made
        # TODO: sometimes moves twice per frame
        direction = "down"

    timer += 1
    pygame.display.update()
    clock.tick(60)
    