class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nums1 = sorted(nums,reverse=True)
        n = len(nums); count = 0
        for i in range(n-1,-1,-1):
            if nums1[i] != 0:
                return count
            elif nums1[i] == 0 and nums[i] != nums1[i]:
                count += 1
        return count
        