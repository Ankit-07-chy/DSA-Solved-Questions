# tabulation with space optimization
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev2 = 1; prev1 = 2; curr =2 
        for i in range(3,n+1):
            curr = prev2 + prev1
            temp = prev1
            prev1 = curr
            prev2 = temp
        return curr

"""
# tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [-1] *(n+1)
        ways[0] = 0
        ways[1] = 1; 
        if n <= 1:
            return ways[n]
        ways[2] = 2
        for i in range(3,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n] """

'''
# memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [-1]*(n+1)
        ways[0] = 0
        def way(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if ways[n] == -1:
                ways[n] = way(n-1) + way(n-2)
            return ways[n]
        return way(n)
        '''
"""
# recursion proper
class Solution:
    def climbStairs(self, n: int) -> int:
        def ways(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            return ways(n-1)  +  ways(n-2)
        return ways(n)
        """