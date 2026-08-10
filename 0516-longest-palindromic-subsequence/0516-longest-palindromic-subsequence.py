class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[0]*(n+1) for i in range(n+1)]
        if n == 1:
            return 1
        # For I we need loop in n-1 to -1 ; for j we need loop from 1 to n
        for i in range(n-1,-1,-1):
            for j in range(1,n):
                if i > j:
                    dp[i][j] = 0
                elif s[i] == s[j] and i != j:
                    dp[i][j] = 2 + dp[i+1][j-1]
                elif s[i] == s[j]  and i == j:
                    dp[i][j] = 1 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                ans = max(ans,dp[i][j])
        return ans
                
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[None]*(n+1) for i in range(n+1)]
        def recursion(i,j):
            
            if i > j :
                return 0

            if dp[i][j] == None:
                if s[i] == s[j] and i != j:
                    dp[i][j] =  2 + recursion(i+1,j-1)
                    return dp[i][j]
                elif s[i] == s[j] and i == j:
                    dp[i][j] = 1 + recursion(i+1,j-1)
                    return dp[i][j]
                else:
                    dp[i][j] = max(recursion(i+1,j),recursion(i,j-1))
                    return dp[i][j]
            return dp[i][j]
        
        return recursion(0,n-1)'''