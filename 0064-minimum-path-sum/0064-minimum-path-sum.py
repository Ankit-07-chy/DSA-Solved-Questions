# Tabulation - Bottom Up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0 :
                    dp[i][j] = grid[i][j]
                elif i > 0 and j < 1:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif i < 1 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]
                    

# Recursion + memoization
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m= len(grid); n = len(grid[0])
        dp = [[-1]*(n+1) for i in range(m+1)]
        def find(dp,grid,row,col):
            if row == 0 and col == 0:
                return grid[row][col]
            if row < 0 or col < 0:
                return float('inf')
            if dp[row][col] == -1:
                p1 = find(dp,grid,row-1,col) + grid[row][col]
                p2 = find(dp,grid,row,col-1)+ grid[row][col]
                dp[row][col] = min(p1,p2)
            return dp[row][col]
        return find(dp,grid,m-1,n-1)"""


# recursion Approach with TLE
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def find(grid,row,col):
            if row == 0 and col == 0:
                return grid[row][col]
            if row < 0 or col < 0:
                return float('inf')
            p1 = grid[row][col] + find(grid,row-1,col)
            p2 = grid[row][col] + find(grid,row,col-1)
            return min(p1,p2)
        return find(grid,len(grid)-1,len(grid[0])-1)'''