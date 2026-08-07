class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height)
        dp = [0]*(n+2)
        for i in range(1,n):
            one = dp[i-1] + abs(height[i]-height[i-1])
            two = float('inf')
            if i > 1:
                two = dp[i-2] + abs(height[i]-height[i-2])
            dp[i] = min(one,two)
        return dp[n-1]
        
        
        
        '''
        def recursion(idx):
            if idx == 0:
                return 0
            one = recursion(idx-1) + abs(height[idx]-height[idx-1])
            two = float('inf')
            if idx > 1:
                two = recursion(idx-2) + abs(height[idx]-height[idx-2])
            return min(one,two)
        n = len(height)
        return recursion(n-1)'''