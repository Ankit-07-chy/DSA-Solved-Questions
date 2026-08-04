class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # go to each 1 which are on boundary side, and then mark them and also make dfs for them

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for i in range(rows)]

        def dfs(i,j):
            idxs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for new_i,new_j in idxs:
                if 0<=new_i<rows and 0<=new_j<cols and visited[new_i][new_j] == 0 and grid[new_i][new_j] == 1:
                    visited[new_i][new_j] = 1
                    dfs(new_i,new_j)
            

        # go for each boundary element only those are 1 and mark them
        for i in range(rows):
            if grid[i][0] == 1 and visited[i][0] == 0:
                visited[i][0] = 1
                dfs(i,0)
            if grid[i][cols-1] == 1 and visited[i][cols-1] == 0:
                visited[i][cols-1] = 1
                dfs(i,cols-1)

        for i in range(cols):
            if grid[0][i] == 1 and visited[0][i] == 0:
                visited[0][i] = 1
                dfs(0,i)
            if grid[rows-1][i] == 1 and visited[rows-1][i] == 0:
                visited[rows-1][i] = 1
                dfs(rows-1,i)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1

        print(visited)
        return count