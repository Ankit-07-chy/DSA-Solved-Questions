class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums)//2
        count = 0
        for num in nums:
            if num == nums[mid]:
                count += 1
        return count == 1