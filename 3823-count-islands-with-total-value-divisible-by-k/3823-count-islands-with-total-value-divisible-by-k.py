class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid); cols = len(grid[0])
        count = 0
        visited = [[0]*cols for i in range(rows)]

        def bfs(i,j):
            visited[i][j] = 1
            current = grid[i][j]
            queue = deque([])

            queue.append([i,j])

            while queue:
                i_,j_ = queue.popleft()
                adj = [(i_+1,j_),(i_-1,j_),(i_,j_+1),(i_,j_-1)]

                for new_i,new_j in adj:
                    if 0<=new_i<rows and 0<=new_j<cols and (visited[new_i][new_j] == 0) and grid[new_i][new_j] != 0:
                        visited[new_i][new_j] = 1
                        current += grid[new_i][new_j]
                        queue.append([new_i,new_j])

            return current % k == 0
        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and grid[i][j] != 0:
                    t = bfs(i,j)
                    if t:
                        count += 1
        return count
