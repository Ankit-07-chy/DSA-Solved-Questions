class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1); n2 = len(text2)
        dp = [[0]*(n2+1) for i in range(n1+1)]

        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

# recursion + memoization
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1); n2 = len(text2)
        dp = [[None]*(n2+1) for i in range(n1+1)]

        def recursion(i,j):
            if i >= n1 or j >= n2:
                return 0

            if dp[i][j] == None:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + recursion(i+1,j+1)
                    return dp[i][j]
                else:
                    t1 = recursion(i+1,j)
                    t2 = recursion(i,j+1)
                    dp[i][j] = max(t1,t2)
                    return dp[i][j]
            return dp[i][j]
        
        return recursion(0,0)
"""

'''
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D Dp Problem it is , lets do recursion first then will memoize it
        n1 = len(text1); n2 = len(text2)

        @cache
        def recursion(i,j):
            if i >= n1 or j >= n2:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + recursion(i+1,j+1)
            else:
                t1 = recursion(i+1,j)
                t2 = recursion(i,j+1)
                return max(t1,t2)
                
        return recursion(0,0)'''