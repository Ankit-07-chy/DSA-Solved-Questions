class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for i in range(32):
            count = 0
            for j in range(0,len(nums)):
                if nums[j] & (1<<i):
                    count += 1
            count = count % 3
            result = result | (count << i)
        if result >= (1<<31):
            result -= (1<<32)
        
        return result