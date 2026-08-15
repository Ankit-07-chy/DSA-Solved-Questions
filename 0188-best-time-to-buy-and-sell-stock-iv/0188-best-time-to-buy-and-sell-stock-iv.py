class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # dp like K(Transactions), Buy or Sold, idx
        n = len(prices)
        dp = [[[None for i in range(k+1)] for i in range(2)] for i in range(n+1)]

        def recursion(idx,buy,cap):
            if cap == 0:
                return 0
            if idx >= n:
                return 0
            if dp[idx][buy][cap] == None:
                if buy :
                    p1 = -prices[idx] + recursion(idx+1,0,cap)
                    p2 = recursion(idx+1,1,cap)
                else:
                    p1 = prices[idx] + recursion(idx+1,1,cap-1)
                    p2 = recursion(idx+1,0,cap)
            
                dp[idx][buy][cap] = max(p1,p2)
            return dp[idx][buy][cap]
        return recursion(0,1,k)