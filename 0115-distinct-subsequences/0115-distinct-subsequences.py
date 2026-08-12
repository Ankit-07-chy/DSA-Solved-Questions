class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s); m = len(t)
        dp = [[None]*(m+1) for i in range(n+1)]
        def recursion(i,j):
            if j < 0:
                return 1
            elif i < 0:
                return 0
            elif s[i] == t[j]:
                if dp[i][j] == None:
                    dp[i][j] = recursion(i-1,j-1) + recursion(i-1,j)
                return dp[i][j]
            else:
                if dp[i][j] == None:
                    dp[i][j] = recursion(i-1,j)
                return dp[i][j]
        return recursion(n-1,m-1)


# python inbuilt cache/ Memo
'''
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n = len(s); m = len(t)
        i = n-1; j = m-1
        
        @cache
        def recursion(i,j):
            if j < 0:
                return 1
            elif i < 0:
                return 0
            elif s[i] == t[j]:
                return recursion(i-1,j-1) + recursion(i-1,j)
            else:
                return recursion(i-1,j)

        return recursion(i,j)
            '''