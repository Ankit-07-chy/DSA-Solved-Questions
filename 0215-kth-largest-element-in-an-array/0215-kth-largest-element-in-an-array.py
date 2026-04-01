class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        # With Sorting
        nums.sort()
        return nums[-k]