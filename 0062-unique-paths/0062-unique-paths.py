# Tabulation - Bottom up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    down = 0; right = 0
                    if i > 0: down = dp[i-1][j]
                    if j > 0: right = dp[i][j-1]
                    dp[i][j] = down + right
        return dp[m-1][n-1]

# recursion with memo
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for i in range(m+1)]
        def find(i,j,dp):
            if i>m or j>n :
                return 0
            if i == m-1 and j== n-1:
                return 1
            if dp[i][j] == -1:
                dp[i][j] = find(i+1,j,dp)+find(i,j+1,dp)
            return dp[i][j]
        return find(0,0,dp)"""
# recursion Approach
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def find(i_idx,j_idx,row,col):
            if i_idx >= row or j_idx >= col:
                return 0
            
            if i_idx == row-1 and j_idx == col-1:
                return 1
            return find(i_idx,j_idx+1,row,col) + find(i_idx+1,j_idx,row,col)
        return find(0,0,m,n)'''