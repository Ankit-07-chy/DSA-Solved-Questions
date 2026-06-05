class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0; maxi = -inf; mini = inf; curr_ = 0
        n = len(nums)
        for i in range(n):
            curr += nums[i]
            curr_ += nums[i]

            if curr >= maxi:
                maxi = curr
            if curr<0:
                curr = 0 
            
            if curr_ < mini:
                mini = curr_
            if curr_ > 0:
                curr_ = 0
        return max(abs(maxi),abs(mini))