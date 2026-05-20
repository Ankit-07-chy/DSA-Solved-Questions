# Memoization 
class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        def cost(height,idx,c):
            if idx == 0:
                return 0
            
            if dp[idx] == -1:
                step1 = cost(height,idx-1,c) + abs(height[idx]-height[idx-1])
                step2 = float('inf')
                if idx > 1:
                    step2 = cost(height,idx-2,c) + abs(height[idx]-height[idx-2])
                
                dp[idx] = min(step1,step2)
            return dp[idx]
            
        dp = [-1]*(n+1)
        return cost(height,len(height)-1,dp)