# Tabulation with space optimization
class Solution:
    def fib(self, n: int) -> int:
        prev2 = 0; prev1 = 1; 
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2,n+1):
            curr = prev1 + prev2
            temp = prev1
            prev1 = curr
            prev2 = temp
        return curr
"""
# Tabulation
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        if n == 0:
            return 0
        dp[0] = 0; dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
"""
'''
# memoization
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fibb(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if dp[n] == -1:
                dp[n] = fibb(n-1) + fibb(n-2)
            return dp[n]
        return fibb(n)
        '''
"""
# normal method
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)

        """