from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recursion(idx,buy):
            if idx >= n:
                return 0 

            if buy:
                p1 = -prices[idx] + recursion(idx+1,0)
                p2 = recursion(idx+1,1)
            else:
                p1 = prices[idx] + recursion(idx+2,1)
                p2 = recursion(idx+1,0)
            return max(p1,p2)

        return recursion(0,1)