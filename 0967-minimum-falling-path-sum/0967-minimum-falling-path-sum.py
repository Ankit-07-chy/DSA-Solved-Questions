# Tabulation for This
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix); m = len(matrix[0])
        dp = [[None]*m for i in range(n)]
        dp[0] = matrix[0][:]
        for i in range(1,n):
            for j in range(0,m):
                st = matrix[i][j] + dp[i-1][j]
                left = inf; right = inf
                if j >= 1:
                    left = matrix[i][j] + dp[i-1][j-1]
                if j < m - 1:
                    right = matrix[i][j] + dp[i-1][j+1]
                dp[i][j] = min(st,left,right)
        return min(dp[n-1])

# Recursion + memoization
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix); m = len(matrix[0])
        dp = [[None]*m for i in range(n)]
        def find(dp,i,j):
            if j < 0 or j >= m:
                return inf
            if i == 0:
                return matrix[i][j]
            if dp[i][j] is None:
                st = find(dp,i-1,j) + matrix[i][j]
                left = find(dp,i-1,j-1) + matrix[i][j]
                right = find(dp,i-1,j+1) + matrix[i][j]
                dp[i][j] = min(st,left,right)
            return dp[i][j]
        mini = inf
        for i in range(m):
            mini = min(mini,find(dp,n-1,i))
        return mini
"""
# recursion Approach with TLE
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix); m = len(matrix[0])
        def find(i,j):
            if j < 0 or j >= m:
                return inf
            if i == 0 :
                return matrix[i][j]
            st = find(i-1,j) + matrix[i][j]
            left = find(i-1,j-1)+ matrix[i][j]
            right = find(i-1,j+1)+ matrix[i][j]
            return min(st,left,right)
        mini = inf
        for i in range(m):
            mini = min(mini,find(n-1,i))
        return mini'''