class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        ans = [-1]*n
        
        # greater element
        # monotnoic dec stack need
        i = n-1
        stack = []
        while i >= 0:
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(arr[i])
            
            
            i -= 1
        return ans