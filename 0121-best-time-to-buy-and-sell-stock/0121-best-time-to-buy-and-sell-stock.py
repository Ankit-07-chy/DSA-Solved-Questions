class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        mini = prices[0]
        for p in prices:
            profit = max(profit,p-mini)
            mini = min(p,mini)
        return profit