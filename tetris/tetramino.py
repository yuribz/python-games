import pygame, sys, random

class Tetramino:
    figures = {
        "I": [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0]
            ],
        "L":  [
            [2, 0, 0],
            [2, 0, 0],
            [2, 2, 0],
            ],
        "J":  [
            [0, 3, 0],
            [0, 3, 0],
            [3, 3, 0],
            ],
        "S":  [
            [0, 4, 4],
            [4, 4, 0],
            [0, 0, 0],
            ],
        "Z":  [
            [5, 5, 0],
            [0, 5, 5],
            [0, 0, 0],
            ],
        "T":  [
            [6, 0, 0],
            [6, 6, 0],
            [6, 0, 0]
            ],
        "O":  [
            [7, 7],
            [7, 7]
            ]
    }

    def __init__(self, shape, x = 5, y = 0):
        self.shape = shape
        self.matrix = list(Tetramino.figures[self.shape]) # make a deep copy
        self.x = x
        self.y = y
    
    def move(self, grid, direction = "down"):

        if self.check_collision(grid, direction):
            return grid
        
        
        # get the lowest non-empty row in the matrix
        row = 0
        while sum(self.matrix[row]) != 0:
            row += 1
            if row >= len(self.matrix):
                break
        
        # remove old blocks
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i >= row:
                    break
                elif self.matrix[i][j] > 0:
                    grid[i + self.y][j + self.x] = 0
        
        # place new blocks with offset
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i >= row:
                    break
                try:
                    if direction == "down":
                        grid[i + self.y + 1][j + self.x] = self.matrix[i][j]
                    if direction == "right":
                        grid[i + self.y][j + self.x + 1] = self.matrix[i][j]
                    if direction == "left":
                        grid[i + self.y][j + self.x - 1] = self.matrix[i][j]
                except IndexError:
                    return grid
        
        # could I do this in one nested loop? yes!
        # was it much harder to do? also yes!
        
        if direction == "down":
            self.y += 1
        elif direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -= 1
        
        return grid
    
    def check_collision(self, grid, direction = "down", x = None, y = None):
        if x == None or y == None:
            x = self.x
            y = self.y
        if direction == "down":
            # get the lowest non-empty row in the matrix
            row = 0
            while sum(self.matrix[row]) != 0:
                row += 1
                if row >= len(self.matrix):
                    break


            # check for any bricks below
            for j in range(len(self.matrix[row - 1])):
                try:
                    if grid[y + row][x + j] > 0:
                        return True
                except IndexError as e:
                    # out of bounds, end of grid, automatic collision
                    return True
            # no collides, return false, keep going
            return False
        return False
