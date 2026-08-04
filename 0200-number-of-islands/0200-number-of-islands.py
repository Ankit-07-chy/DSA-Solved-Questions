class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 -> Land, 0 -> water
        # no of islands
        rows = len(grid); cols = len(grid[0])
        visited = [[0]*cols for i in range(rows)]
        count = 0

        def dfs(i,j):
            idxs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for new_i,new_j in idxs:
                if 0<=new_i<rows and 0<=new_j <cols and visited[new_i][new_j] == 0 and grid[new_i][new_j] == '1':
                    visited[new_i][new_j] = 1
                    dfs(new_i,new_j)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    visited[i][j] = 1
                    dfs(i,j)
                    count += 1
        print(visited)
        return count
