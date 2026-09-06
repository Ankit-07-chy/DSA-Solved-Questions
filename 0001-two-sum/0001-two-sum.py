class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        n = len(nums)
        for i in range(n):
            remain = target - nums[i]
            if remain in freq:
                return [freq[remain],i]
            freq[nums[i]] = i