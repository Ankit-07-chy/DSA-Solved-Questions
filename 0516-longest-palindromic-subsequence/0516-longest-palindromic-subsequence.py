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
        
        return recursion(0,n-1)