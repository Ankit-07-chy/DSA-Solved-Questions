class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [] # Monotonic dec stack
        i = n-1
        while i >= 0:
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            stack.append(nums[i])
            i -= 1

        ans = [-1]*n
        i = n-1
        while i >= 0:
            while stack and stack[-1]<=nums[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
            i -= 1
        return ans