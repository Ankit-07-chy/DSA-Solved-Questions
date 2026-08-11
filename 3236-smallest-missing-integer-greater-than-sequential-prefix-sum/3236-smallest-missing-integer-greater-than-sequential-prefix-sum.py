class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1; curr_sum = nums[0]
        seen = set(nums)

        while i < n:
            if nums[i] == nums[i-1] + 1:
                curr_sum += nums[i]
            else:
                break
            i += 1
        print(curr_sum)
        t = curr_sum
        while True:
            if t not in seen:
                return t 
            else:
                t += 1
