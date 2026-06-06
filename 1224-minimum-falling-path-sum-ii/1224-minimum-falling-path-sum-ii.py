# Tabulation 
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[inf]*n for i in range(n)]
        dp[0] = grid[0][:]
        for i in range(1,n):
            for j in range(n):
                for c in range(n):
                    if c != j:
                        dp[i][j] = min(dp[i][j], grid[i][j]+dp[i-1][c])
        return min(dp[n-1])


# recursion with memo
"""
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[None]*n for i in range(n)]
        def find(dp,i,j):
            if j < 0 or j > n-1:
                return inf
            if i == 0:
                return grid[i][j]
            if dp[i][j] is None:
                mini = inf
                for c in range(n):
                    if c != j:
                        mini = min(mini,grid[i][j]+find(dp,i-1,c))
                dp[i][j] = mini
            return dp[i][j]
        m = inf
        for i in range(n):
            m = min(m,find(dp,n-1,i))
        return m


"""
# recursion with TLE
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def find(i,j):
            if j < 0 or j > n - 1:
                return inf
            if i == 0:
                return grid[i][j]
            mini = inf
            for c in range(n):
                if c != j:
                    mini = min(mini,grid[i][j] + find(i-1,c))
            return mini
        m  = inf
        for i in range(n):
            m = min(m,find(n-1,i))
        return m'''