# Optimal One
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        stack = []
        for i in range(n):
            if not stack or nums[stack[-1]]>=nums[i]:
                stack.append(i)
        # monotonic dec stack

        j = n-1
        while j >= 0:
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans,j-stack[-1])
                stack.pop()
            j -= 1
        return ans

        

# brute force approach
'''
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<=nums[j]:
                    ans = max(ans,j-i)
        return ans'''