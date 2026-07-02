from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        health_grid = [[-1] * n for _ in range(m)]
        start_health = health - grid[0][0]
        
        if start_health < 0:
            return False
            
        health_grid[0][0] = start_health
        q = deque([(0, 0, start_health)])  # Store health in queue!
        
        while q:
            i, j, current_health = q.popleft()
            
            if i == m-1 and j == n-1:
                return True
            
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_health = current_health - grid[ni][nj]
                    if new_health > health_grid[ni][nj] and new_health > 0:  # Only track better health
                        health_grid[ni][nj] = new_health
                        q.append((ni, nj, new_health))
        
        return health_grid[m-1][n-1] >= 0