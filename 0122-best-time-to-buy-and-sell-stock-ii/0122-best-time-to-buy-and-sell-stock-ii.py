# recursion + Memo
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