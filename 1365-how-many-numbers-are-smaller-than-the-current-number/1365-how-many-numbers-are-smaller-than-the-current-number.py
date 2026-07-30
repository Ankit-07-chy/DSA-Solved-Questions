class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(0,n):
            count = 0
            for j in range(0,n):
                if nums[i]>nums[j] and i != j:
                    count += 1
            result.append(count)
        return result