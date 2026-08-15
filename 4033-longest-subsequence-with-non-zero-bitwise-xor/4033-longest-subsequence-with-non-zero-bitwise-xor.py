class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # subsequence --> Means element in b/w can be missing
        total_xor = 0
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            total_xor = total_xor ^ num

        if zero_count == len(nums):
            return 0 
        if total_xor != 0:
            return len(nums)
        for num in nums:
            if total_xor ^ num != 0:
                return len(nums) - 1