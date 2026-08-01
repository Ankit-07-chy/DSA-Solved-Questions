class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*n

        for query in queries:
            start = query[0]; end = query[1]+1; val = -1
            diff[start] += val
            if end < n:
                diff[end] -= val

        for i in range(1,n):
            diff[i] += diff[i-1]

        for i in range(0,n):
            if nums[i]>-diff[i]:
                return False
        return True
        
        