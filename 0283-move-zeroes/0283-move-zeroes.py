class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first_zero_idx = -1
        for u,v in enumerate(nums):
            if v == 0:
                first_zero_idx = u
                break
        if first_zero_idx != -1:
            n = len(nums)
            j = first_zero_idx + 1
            while j < n:
                if nums[j] != 0:
                    nums[first_zero_idx] = nums[j]
                    first_zero_idx += 1
                j += 1
            for t in range(first_zero_idx,n):
                nums[t] = 0