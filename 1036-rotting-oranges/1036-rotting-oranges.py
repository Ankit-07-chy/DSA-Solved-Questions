from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid); col = len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        q = deque([]) # at time = 0, the things which are rotten have put in this queue
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j,0]) # [row,col,time]
                    visited[i][j] = 2

        curr_time = 0
        while q:
            t = q.popleft()
            curr_time = max(curr_time,t[-1])
            # adjacent directions
            adj = [[t[0]+1,t[1]],[t[0]-1,t[1]],[t[0],t[1]+1],[t[0],t[1]-1]]
            for ad in adj:
                if 0<=ad[0]<row and 0<=ad[1]<col:
                    if grid[ad[0]][ad[1]] == 1:
                        q.append([ad[0],ad[1],t[-1]+1])
                        visited[ad[0]][ad[1]] = 2
                        grid[ad[0]][ad[1]] = 2  # Update the grid
        for i in range(row):
            for j in range(col):
                if grid[i][j] != visited[i][j]:
                    return -1
        return curr_time


