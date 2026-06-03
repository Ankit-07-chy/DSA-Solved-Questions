class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for u in nums:
            if u in freq:
                freq[u] += 1
            else:
                freq[u] = 1
        for key,val in freq.items():
            if val >= 2:
                return key