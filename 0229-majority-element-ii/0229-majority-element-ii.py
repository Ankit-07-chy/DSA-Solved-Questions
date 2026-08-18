import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        result = []
        n = len(nums)
        for u,v in freq.items():
            if n//3 < v:
                result.append(u)
        return result