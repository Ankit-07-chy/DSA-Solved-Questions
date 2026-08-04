from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        # 0 -> land; 1 -> water
        queue = deque([])
        ans = [[-1] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    queue.append([i, j])
                    ans[i][j] = 0
        # bfs here
        while queue:
            i, j = queue.popleft()
            adj = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for new_i, new_j in adj:
                if 0 <= new_i < rows and 0 <= new_j < cols and ans[new_i][new_j] == -1:
                    ans[new_i][new_j] = ans[i][j] + 1
                    queue.append([new_i, new_j])
        return ans
