# Tabulation Method with space Optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next_0,next_1 = 0,0
        for i in range(n-1,-1,-1):
         
            curr_1 = max(-prices[i]+next_0,next_1)
            curr_0 = max(prices[i]+next_1,next_0)
            next_0,next_1 = curr_0,curr_1
        return next_1



# Tabulation Method
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n+1)]


        for i in range(n-1,-1,-1):
            for j in range(1,-1,-1):
                if j == 1:
                    dp[i][j] = max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i]+dp[i+1][1], dp[i+1][0])
        return dp[0][1]

'''
# recursion + Memo
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[None]*2 for i in range(n)]

        def f(idx,buy) :
            # buy -> 1 and 0
            if idx >= n:
                return 0
            if dp[idx][int(buy)] == None:
                if buy :
                    p1 = -prices[idx] + f(idx+1,False)
                    p2 = f(idx+1,True)
                else:
                    p1 = prices[idx] + f(idx+1,True)
                    p2 = f(idx+1,False)

                dp[idx][int(buy)] = max(p1,p2)
            
            return dp[idx][int(buy)]
        return f(0,True)
"""
'''
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def f(idx,buy) :
            if idx >= n:
                return 0
            
            if buy: # True
                p1 = -prices[idx]+f(idx+1,False)
                p2 = f(idx+1,True)
            else: # sell
                p1 = prices[idx] + f(idx+1, True)
                p2 = f(idx+1, False)
            
            return max(p1,p2)
        return f(0,True)'''