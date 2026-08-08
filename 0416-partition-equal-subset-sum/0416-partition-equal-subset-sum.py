class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2 != 0:
            return False
        dp = [[None]*(total_sum+1) for i in range(n+1)]

        def recursion(idx,curr_sum):
            if curr_sum == total_sum - curr_sum:
                return True
            if idx < 0:
                return False
            if dp[idx][curr_sum] == None:
                pick = recursion(idx-1,curr_sum + nums[idx])
                not_pick = recursion(idx-1,curr_sum)
                dp[idx][curr_sum] = pick or not_pick
            return dp[idx][curr_sum]
        return recursion(n-1,0)