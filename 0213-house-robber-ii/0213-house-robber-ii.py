# Tabulation 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [-1]*n
        # leave last one and put remaing
        dp[0]= nums[0]
        start = 0; last = n-2 # Boundary
        for i in range(start+1,last+1):
            pick = nums[i]
            if i > 1:
                pick += dp[i-2]
            not_pick = dp[i-1]
            dp[i] = max(pick,not_pick)
        ans1 = dp[n-2]

        # leave 1st and put remaining
        dp = [-1]*n
        dp[0] = 0; dp[1] = nums[1]
        start = 1; last = n-1 # boundary
        for i in range(start+1,last+1):
            pick = nums[i]
            if i > 1:
                pick += dp[i-2]
            not_pick = dp[i-1]
            dp[i] = max(pick,not_pick)
        ans2 = dp[n-1]
        return max(ans1,ans2)

# Memoization on Recursion wala Approach
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        def find_seq(dp,arr,idx,boundary):
            if idx <= boundary:
                return 0
            if idx == boundary+1:
                return arr[idx]
            
            if dp[idx]==-1:
                pick = arr[idx] + find_seq(dp,arr,idx-2,boundary)
                not_pick = 0+find_seq(dp,arr,idx-1,boundary)
                dp[idx] = max(pick,not_pick)
            return dp[idx]

        # Leaveout Last and find out for remaing
        dp1 = [-1]*(n)
        ans1 = find_seq(dp1,nums,len(nums)-2,-1) # taht 0 is starting boundary

        # Leaveout the first and find out for remaining
        dp1 = [ -1]*(n)
        ans2 = find_seq(dp1,nums,len(nums)-1,0) # that 1 is starting boundary
        return max(ans1,ans2)
        '''