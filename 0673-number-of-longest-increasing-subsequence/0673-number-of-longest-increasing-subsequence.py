class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1]*n
        count = [1]*n
        maxi = 1
        for i in range(0,n):
            for prev in range(0,i):
                if nums[i] > nums[prev] and dp[i] < dp[prev] + 1:
                    dp[i] = 1 + dp[prev]
                    count[i] = count[prev]
                elif nums[i] > nums[prev] and dp[i] == dp[prev] + 1:
                    count[i] += count[prev]
            maxi = max(maxi,dp[i])
        ans = 0
        for i in range(0,n):
            if dp[i] == maxi:
                ans += count[i]
        return ans
