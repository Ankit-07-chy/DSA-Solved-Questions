class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        maxLen = 0
        for char in s:
            if char == '(':
                # stack.append('(')
                stack += 1
                maxLen = max(maxLen,stack)
            elif char == ')':
                stack -= 1
        return maxLen

'''
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxLen = 0
        for char in s:
            if char == '(':
                stack.append('(')
                maxLen = max(maxLen,len(stack))
            elif char == ')':
                stack.pop()
        return maxLen
'''