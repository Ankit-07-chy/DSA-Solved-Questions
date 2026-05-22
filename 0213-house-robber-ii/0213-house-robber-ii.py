# Memoization on Recursion wala Approach

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
        