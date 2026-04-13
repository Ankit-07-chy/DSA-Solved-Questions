class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        m = float('inf')
        for i in range(start,n):
            if nums[i] == target:
                m = min(m,abs(i-start))
        for j in range(start,-1,-1):
            if nums[j]==target:
                m = min(m,abs(j-start))
        return m