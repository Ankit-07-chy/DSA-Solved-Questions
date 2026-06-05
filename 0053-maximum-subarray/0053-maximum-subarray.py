class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0; maxi = -inf
        n = len(nums)
        for i in range(n):
            curr += nums[i]
            if curr > maxi:
                maxi = curr
            if curr < 0:
                curr =0
        return maxi
