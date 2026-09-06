class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        prev = 0
        i = 0; n = len(nums)
        while i<n:
            if nums[i] == 0:
                nums[i],nums[prev] = nums[prev],nums[i]
                prev += 1
            i += 1
        i = n-1
        next = n-1
        while i>=0:
            if nums[i]==2:
                nums[i],nums[next] = nums[next],nums[i]
                next -= 1
            i -= 1