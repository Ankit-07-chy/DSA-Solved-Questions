class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1 = nums[-1]; n2 = nums[-2]; n3 = nums[0]; n4 = nums[1]
        l1 = (n1-1)*(n2-1)
        l2 = (n3-1)*(n4-1)
        return max(l1,l2)