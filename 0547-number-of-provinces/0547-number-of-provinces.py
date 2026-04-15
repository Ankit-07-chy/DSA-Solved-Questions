class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def bfs(start):
            row_to_start = isConnected[start]
            for j in range(n):
                if row_to_start[j] == 1 and not visited[j]:
                    visited[j] = True
                    bfs(j)

        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1
                visited[i] = True
                bfs(i)
        return count