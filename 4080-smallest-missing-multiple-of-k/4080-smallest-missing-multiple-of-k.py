class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        i = 1
        while True:
            num = i * k 
            if num not in nums:
                return num
            i += 1