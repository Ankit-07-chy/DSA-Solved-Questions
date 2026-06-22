from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] !=  0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        queue = deque([])
        queue.append([1,0,0])
        visited = [[0]*n for i in range(n)]
        visited[0][0] = 1

        # using BFS
        while queue:
            temp = queue.popleft()
            dist = temp[0]; i = temp[1]; j = temp[2]

            if i == n-1 and j == n-1:
                return dist
            indexes = [[i+1,j],[i+1,j+1],[i+1,j-1],[i,j+1],[i,j-1],[i-1,j],[i-1,j+1],[i-1,j-1]]

            for index in indexes:
                if 0<=index[0]<n and 0<=index[1]<n:
                    if visited[index[0]][index[1]] == 0 and grid[index[0]][index[1]]==0:
                        visited[index[0]][index[1]] = 1
                        queue.append([dist+1,index[0],index[1]])

        return -1 