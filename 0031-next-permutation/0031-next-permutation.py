class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakpoint = -1
        n = len(nums)
        def reverse(nums):
            left = 0; right = len(nums)-1
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        for i in range(n-1,0,-1):
            if nums[i-1]< nums[i]:
                breakpoint = i - 1
                break
        m = inf; idx = -1
        def r(arr,i1,i2):
            while i1 < i2:
                nums[i1],nums[i2] = nums[i2],nums[i1]
                i1 += 1
                i2 -= 1
        if breakpoint != -1:
            for i in range(n-1,breakpoint-1,-1):
                if nums[i] > nums[breakpoint]:
                    nums[i],nums[breakpoint] = nums[breakpoint], nums[i]
                    break
            r(nums,breakpoint+1,n-1)
        else:
            reverse(nums)
