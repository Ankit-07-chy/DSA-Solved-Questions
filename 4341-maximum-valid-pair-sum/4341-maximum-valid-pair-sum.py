class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        best = nums[0]
        ans = 0

        for j in range(k,len(nums)):
            best = max(best,nums[j-k])
            ans = max(ans,best+nums[j])
        return ans