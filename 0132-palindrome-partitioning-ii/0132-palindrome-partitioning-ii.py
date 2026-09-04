# precomputing for palindrome
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False]*n for i in range(n)]

        # Length 1
        for i in range(n):
            pal[i][i] = True

        # Length >= 2
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or pal[i + 1][j - 1]:
                        pal[i][j] = True
        
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            t = 10**8 
            for j in range(i,n):
                if pal[i][j]:
                    t = min(t,1+dp[j+1])
            dp[i] = t
        return dp[0] - 1


"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        def palindrome(i,j):
            while i <= j:
                if s[i]!=s[j]:
                    return False
                i += 1; j -= 1
            return True
        
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            t = 10**8 
            for j in range(i,n):
                if palindrome(i,j):
                    t = min(t,1+dp[j+1])
            dp[i] = t
        return dp[0] - 1
"""

'''
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        def palindrome(i,j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1; j -= 1
            return True

        @cache
        def f(i):
            if i >= n:
                return 0
            t = 10**8
            for j in range(i,n):
                if palindrome(i,j):
                    t = min(t,1+f(j+1))
            return t
        return f(0) - 1
'''