# Optimal Approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointer
        n = len(nums)
        low = 0; mid = 0; high = n - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high]= nums[high],nums[mid]
                high -= 1



# Better Approach
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0; one_count = 0; two_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            elif n == 1:
                one_count += 1
            else:
                two_count += 1
        for i in range(0,zero_count):
            nums[i] = 0
        for i in range(zero_count,one_count+zero_count):
            nums[i] = 1
        for i in range(one_count+zero_count,one_count+zero_count+two_count):
            nums[i] = 2'''