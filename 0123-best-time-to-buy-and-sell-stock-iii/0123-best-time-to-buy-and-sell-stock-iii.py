class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[0 for _ in range(3)] for _ in range(2)]
              for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            # ---------- cap = 1 ----------
            # buy = 1
            p1 = -prices[i] + dp[i+1][0][1]
            p2 = dp[i+1][1][1]
            dp[i][1][1] = max(p1, p2)

            # buy = 0
            p3 = prices[i] + dp[i+1][1][0]
            p4 = dp[i+1][0][1]
            dp[i][0][1] = max(p3, p4)


            # ---------- cap = 2 ----------
            # buy = 1
            p1 = -prices[i] + dp[i+1][0][2]
            p2 = dp[i+1][1][2]
            dp[i][1][2] = max(p1, p2)

            # buy = 0
            p3 = prices[i] + dp[i+1][1][1]
            p4 = dp[i+1][0][2]
            dp[i][0][2] = max(p3, p4)

        return dp[0][1][2]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[None for _ in range(4)] for _ in range(3)] for _ in range(n+1)]

        def recursion(idx,buy,cap): # dp[n][2][3]
            if cap == 0:
                return 0
            if idx >= n:
                return 0
            if dp[idx][buy][cap] == None:
                if buy:
                    p1 = -prices[idx] + recursion(idx+1,0,cap)
                    p2 = recursion(idx+1,1,cap)
                else:
                    p1 = prices[idx] + recursion(idx+1,1,cap-1)
                    p2 = recursion(idx+1,0,cap)
                dp[idx][buy][cap] = max(p1,p2)
                # pass
            return dp[idx][buy][cap]
        return recursion(0,1,2)


'''

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def recursion(idx,buy,cap):
            if cap == 0:
                return 0
            if idx >= n:
                return 0
            
            if (idx,buy,cap) not in dp:

                if buy:
                    p1 = -prices[idx] + recursion(idx+1,False,cap)
                    p2 = recursion(idx+1,True,cap)
                else:
                    p1 = prices[idx] + recursion(idx+1,True,cap-1)
                    p2 = recursion(idx+1,False,cap)

                dp[(idx,buy,cap)] = max(p1,p2)
            return  dp[(idx,buy,cap)] 
        return recursion(0,True,2)



'''
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum transactions can be two mins Mostly 2 Trade Can be done
        n = len(prices)
        # after every sell increase the trade window by one, and while updating the result in that case chekc that also
        trade_window = 0
        @cache
        def recursion(i,buy,cap):
            if cap < 0:
                return -10**9
            if i >= n and cap >= 0:
                return 0

            if buy: # True
                p1 = -prices[i] + recursion(i+1,False,cap)
                p2 = recursion(i+1,True,cap)
            else : 
                # Buy -> False
                p1 = prices[i] + recursion(i+1,True,cap-1)
                p2 = recursion(i+1,False,cap)
                #  trade_window += 1
            return max(p1,p2)
        return recursion(0,True,2)
        '''
        """