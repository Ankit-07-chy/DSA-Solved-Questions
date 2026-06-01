# Tabulation -> is always Opposite of Recursion
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*(i+1) for i in range(n)]
        for idx,val in enumerate(triangle[n-1]):
            dp[n-1][idx] = val
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = dp[i+1][j] + triangle[i][j]
                diag = dp[i+1][j+1] + triangle[i][j]
                dp[i][j] = min(down,diag)
        return dp[0][0]


'''
# Recursion with memo
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None]*(i+1) for i in range(n)]
        def find(dp,row,col):
            if row == n-1:
                return triangle[row][col]
            if dp[row][col] is None:
                down = triangle[row][col] + find(dp,row+1,col)
                diag = triangle[row][col]+find(dp,row+1,col+1)
                dp[row][col] = min(down,diag)
            return dp[row][col]
        return find(dp,0,0)'''
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def find(row,col):
            if row == n-1:
                return triangle[row][col]
            
            down = find(row+1,col)
            diag = find(row+1,col+1)
            return triangle[row][col] + min(down,diag)
            
        return find(0,0)"""
        

# Recursion WIth TLE
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        def find(triangle,idx,row):
            if row == rows-1:
                return triangle[row][idx]
                
            down = find(triangle,idx,row+1)
            diag = find(triangle,idx+1,row+1)
            return triangle[row][idx] + min(down,diag)
            
        return find(triangle,0,0)'''
            