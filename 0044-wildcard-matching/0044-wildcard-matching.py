class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s); m = len(p)
        dp = [[False]*(m+1) for i in range(n+1)]

        dp[0][0] = True
        
        for j in range(1,m+1):
            if p[j-1] == '*':
                dp[0][j] =  dp[0][j-1]

        dp[0][0] = True
        

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[n][m]
        


"""
# recursion + Memo
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s); m = len(p)
        dp = [[None]*(m+1) for i in range(n+1)]

        def recursion(i,j):
            if i < 0 and j < 0:
                return True
            elif i < 0 and j >= 0:
                for ii in range(j,-1,-1):
                    if p[ii] != '*':
                        return False
                return True
            elif j < 0 and i >= 0:
                return False
            elif s[i] == p[j] or p[j] == '?':
                if dp[i][j] == None:
                    dp[i][j] =  recursion(i-1,j-1)
                return dp[i][j]
            elif p[j] == '*':
                if dp[i][j] == None:
                    dp[i][j] = recursion(i,j-1) or recursion(i-1,j)
                return dp[i][j]
            else:
                return False

        return recursion(n-1,m-1)

"""


# python inbuild Cache
'''
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s); m = len(p)

        @cache
        def recursion(i,j):
            # base case
            if i < 0 and j < 0:
                return True
            elif i < 0 and j >= 0:
                for ii in range(j,-1,-1):
                    if p[ii] != '*':
                        return False
                return True
            elif j < 0 and i >= 0:
                return False

            elif s[i]==p[j] or p[j] == '?':
                return recursion(i-1,j-1)
            elif p[j] == '*':
                return recursion(i,j-1) or recursion(i-1,j)
            else:
                return False

        return recursion(n-1,m-1)
        '''