import pygame, sys, random

from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

font = pygame.font.Font(None, 60)
flag = pygame.image.load("assets/flag.png")
flag = pygame.transform.scale(flag, (50, 50))

game = 0

colors = {
    -1: (0, 0, 0),
    0: (0, 0, 0),
    1: (0, 0, 255),      # Blue
    2: (0, 128, 0),      # Green
    3: (255, 0, 0),      # Red
    4: (0, 0, 128),      # Dark blue
    5: (128, 0, 0),      # Dark red
    6: (0, 128, 128),    # Teal
    7: (0, 0, 0),        # Black
    8: (128, 128, 128)   # Dark gray
}

def generate_grid(bombs = 10):
    grid = [[0 for _ in range(10)] for _ in range(10)]
    covers = [[1 for _ in range(10)] for _ in range(10)]

    while bombs:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if grid[y][x] != -1:
            grid[y][x] = -1
            for a in range(x - 1, x + 2):
                for b in range(y - 1, y + 2):
                    try:
                        if (a == x and b == y) or grid[b][a] == -1 or a < 0 or b < 0:
                            continue
                        else:
                            grid[b][a] += 1
                    except:
                        continue
            bombs -= 1
        
    return grid, covers

def flood(x, y, depth):
    if depth == 50 or grid[y][x] > 0:
        return
    else:
        for a in range(x-1, x + 2):
            for b in range(y - 1, y + 2):
                if (a == x and b == y) or a < 0 or b < 0:
                    continue
                else:
                    try:
                        if grid[b][a] == 0 and covers[b][a] == 1:
                            covers[b][a] = 0
                            flood(a, b, depth + 1)
                        elif grid[b][a] > 0:
                            covers[b][a] = 0
                    except:
                        continue


grid, covers = generate_grid()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game == 0:
            pos = pygame.mouse.get_pos()
            i = pos[0] // 50
            j = pos[1] // 50

            buttons = pygame.mouse.get_pressed(num_buttons=3)
            
            if buttons[0]:
                if sum(list(map(sum, covers))) == 100:
                    while grid[j][i] != 0:
                        grid, covers = generate_grid()
                if covers[j][i] == 1:
                    covers[j][i] = 0
                    if grid[j][i] == 0:
                        flood(i, j, 0)

                if grid[j][i] == -1:
                    game = 1
                    
                    
            elif buttons[2]:
                if covers[j][i] == 2:
                    covers[j][i] = 1
                elif covers[j][i] == 1:
                    covers[j][i] = 2
            

    screen.fill((220, 220, 220))

    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, (0, 0, 0), (i * 50, j * 50, 50, 50), width = 1)
            if grid[j][i] != 0:
                num = grid[j][i]
                text = font.render(str(num), True, colors[num])
                textRect = text.get_rect()
                textRect.center = (i * 50 + 25, j * 50 + 25)
                screen.blit(text, textRect)
            
            if covers[j][i] > 0:
                pygame.draw.rect(screen, (150, 150, 150), (i * 50, j * 50, 50, 50))
                pygame.draw.rect(screen, (0, 0, 0), (i * 50, j * 50, 50, 50), width = 1)
            if covers[j][i] == 2:
                screen.blit(flag, (i * 50, j * 50, 50, 50))
    
    if sum([1 for row in covers for cover in row if cover != 0]) == 10:
        # this doesn't work for some reason
        game = 2
    
    if game == 1:
        endgame_font = pygame.font.Font(None, 100)
        text = endgame_font.render("YOU LOSE", True, (200, 0, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (250, 250)
        screen.blit(text, textRect)
    elif game == 2:
        endgame_font = pygame.font.Font(None, 100)
        text = endgame_font.render("YOU WIN", True, (0, 200, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (250, 250)
        screen.blit(text, textRect)
    
    pygame.display.update()