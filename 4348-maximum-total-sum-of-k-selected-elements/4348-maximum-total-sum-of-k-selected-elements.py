class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        # the approach may be different but for now it is given to me that elements are all greater than 1 so its easy in that direction
        nums.sort()
        total_sum = 0; idx = len(nums) - 1
        while k > 0:
            k -= 1
            curr_ele = nums[idx]
            idx -= 1
            if mul > 1:
                total_sum += (mul*curr_ele)
            else:
                total_sum += (curr_ele)
            mul -= 1

            if idx < 0:
                break
        return total_sum