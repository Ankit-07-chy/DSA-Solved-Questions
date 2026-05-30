# Tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    left = 0; right = 0
                    if i > 0: left = dp[i-1][j]
                    if j > 0: right = dp[i][j-1]
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j]=left+right

        return dp[m-1][n-1]


# Recursion + Memo
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        dp = [[-1]*(n+1) for i in range(m+1)]
        def find(dp,obstacleGrid,row,col):
            if row == 0 and col == 0 and obstacleGrid[row][col] != 1:
                return 1
            if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
                return 0
            if dp[row][col] == -1:
                left = find(dp,obstacleGrid,row-1,col)
                right = find(dp,obstacleGrid,row,col-1)
                dp[row][col] = left + right
            return dp[row][col]
        return find(dp,obstacleGrid,m-1,n-1)"""
# Just Recursion Approach 
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        def find(obstacleGrid,i,j):
            if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                return 1
            if i< 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            return find(obstacleGrid,i-1,j) + find(obstacleGrid,i,j-1)
        return find(obstacleGrid,m-1,n-1)'''