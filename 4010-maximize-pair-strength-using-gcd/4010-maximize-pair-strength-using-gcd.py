
# brute force
import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi_st = 0
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                curr = (nums[i]*nums[j])/ (math.gcd(nums[i],nums[j])**2)
                maxi_st = max(maxi_st,curr)

        return int(maxi_st)