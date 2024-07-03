import pygame, sys, time, random
from pygame.locals import QUIT

sx = 50
sy = 50
ax = 450
ay = 450
direction = None

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

start_time = time.time() 

font = pygame.font.Font(None, 16)
timer = 0

snake = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction = "up"
    elif keys[pygame.K_DOWN]:
        direction = "down"
    elif keys[pygame.K_LEFT]:
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        direction = "right"
    
    if timer % 10 == 0:
        snake.append((sx, sy))

        if direction == "up":
            sy -= 25
        elif direction == "down":
            sy += 25
        elif direction == "right":
            sx += 25
        elif direction == "left":
            sx -= 25
        
        snake.pop(0)

    # print(clock.get_fps())
    timer += 1
    timer = int(timer)
    # print(timer)
    # print(clock.tick())
    pygame.draw.rect(screen, (255, 255, 255), (sx, sy, 25, 25))
    pygame.draw.rect(screen, (255, 0, 0), (ax, ay, 25, 25))

    for s in snake:
        pygame.draw.rect(screen, (255, 255, 255), (s[0], s[1], 25, 25))

    if ax == sx and ay == sy:
        ax = (random.randint(0, 475) // 25) * 25
        ay = (random.randint(0, 475) // 25) * 25
        snake.append((sx, sy))
    
    if sx < 0 or sx > 475 or sy < 0 or sy > 475:
        pygame.quit()
        sys.exit()
    
    # text = font.render(str(snake), False, (255, 255, 255))
    # screen.blit(text, pygame.Rect(50, 50, 50, 50))

    pygame.display.update()
    clock.tick(60)