from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = 'E'  # E, N, W, S
        # Directions in clockwise order: East, North, West, South
        self.dir_order = ['E', 'N', 'W', 'S']
        self.dir_names = {'E': 'East', 'N': 'North', 'W': 'West', 'S': 'South'}
        
    def step(self, num: int) -> None:
        # If num is large, we can reduce it modulo the perimeter
        perimeter = 2 * (self.width + self.height - 2)
        if perimeter > 0:
            num = num % perimeter
            if num == 0:
                num = perimeter  # Special case: full circle
        
        while num > 0:
            if self.direction == 'E':
                # Distance to the right wall
                dist_to_wall = (self.width - 1) - self.x
                if num <= dist_to_wall:
                    self.x += num
                    num = 0
                else:
                    self.x = self.width - 1
                    num -= dist_to_wall
                    self.direction = 'N'
                    
            elif self.direction == 'N':
                # Distance to the top wall
                dist_to_wall = (self.height - 1) - self.y
                if num <= dist_to_wall:
                    self.y += num
                    num = 0
                else:
                    self.y = self.height - 1
                    num -= dist_to_wall
                    self.direction = 'W'
                    
            elif self.direction == 'W':
                # Distance to the left wall
                dist_to_wall = self.x
                if num <= dist_to_wall:
                    self.x -= num
                    num = 0
                else:
                    self.x = 0
                    num -= dist_to_wall
                    self.direction = 'S'
                    
            elif self.direction == 'S':
                # Distance to the bottom wall
                dist_to_wall = self.y
                if num <= dist_to_wall:
                    self.y -= num
                    num = 0
                else:
                    self.y = 0
                    num -= dist_to_wall
                    self.direction = 'E'

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir_names[self.direction]