class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l1 = nums[-1]; l2 = nums[-2]; l3 = nums[-3]
        p1 = nums[0]; p2 = nums[1]; p3 = nums[2]
        return max(l1*l2*l3,p1*p2*l1)