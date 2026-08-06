class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1 for i in range(n)]
            def union(self,x,y):
                # here x and y is idx for those in manner like (i*cols + j)
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return 
                if self.size[px] > self.size[py]:
                    self.parent[py] =  px
                    self.size[px] += self.size[py]
                else:
                    self.parent[px] = py
                    self.size[py] += self.size[px]
            
            def find(self,x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
        
        rows = len(grid); cols = len(grid[0])
        dsu = DSU(rows*cols)
        visited = [[False]*cols for i in range(rows)]
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 or visited[i][j] == True:
                    continue
                queue.append([i,j])
                visited[i][j] = True
                while queue:
                    i_,j_ = queue.popleft()
                    idxs = [(i_+1,j_),(i_-1,j_),(i_,j_+1),(i_,j_-1)]
                    for new_i,new_j in idxs:
                        if 0<=new_i<rows and 0<=new_j<cols and visited[new_i][new_j] == False and grid[new_i][new_j] == 1:
                            dsu.union(i*cols+j,new_i*cols+new_j)
                            visited[new_i][new_j] = True
                            queue.append([new_i,new_j])
        ans = 1
        hit = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    hit = True
                    idxs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                    s = set()
                    for new_i,new_j in idxs:
                        if 0<=new_i<rows and 0<=new_j < cols and grid[new_i][new_j] == 1:
                            s.add(dsu.find(new_i*cols+new_j))
                    curr = 1
                    for t in s:
                        curr += dsu.size[t]
                    ans = max(ans,curr)
        if hit:
            return ans
        return rows*cols


# as this solution going for o(n^4)-> so i am expecting tle form this
'''
from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # currently the idea running in my mind is , go to every zero and then run a bfs, start count from 1 for island size

        def find_max_land(i,j,count):
            visited = [[False]*n for i in range(n)]
            visited[i][j] = True
            queue = deque([])
            queue.append([i,j])
            while queue:
                i,j = queue.popleft()
                idxs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for new_i,new_j in idxs:
                    if 0<=new_i<n and 0<=new_j<n and visited[new_i][new_j] == False and grid[new_i][new_j] == 1:
                        visited[new_i][new_j] = True
                        queue.append([new_i,new_j])
                        count += 1
            return count

        ans = 1
        hit = False
        for i in range(n):
            for j in range(n):
                # once I have i,j element as 0 then run bfs, it took o(n*4)
                if grid[i][j] == 0:
                    hit = True
                    ans = max(ans,find_max_land(i,j,1)) 
        if hit:

            return ans
        return n**2'''