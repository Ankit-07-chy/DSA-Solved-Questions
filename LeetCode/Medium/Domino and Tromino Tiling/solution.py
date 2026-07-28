class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # i have to make 2*n board --> ways to return
        n1 = 10
        if n <= 3:
            dp = [0]*(n1+1)
        else:
            dp = [0]*(n+1)
        
        # fxn from derivation we got => f(n) = 2f(n-1) + f(n-3)
        dp[0] = 1; dp[1] = 1; dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % MOD
        return dp[n]
