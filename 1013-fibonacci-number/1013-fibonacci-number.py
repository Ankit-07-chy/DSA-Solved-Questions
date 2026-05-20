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