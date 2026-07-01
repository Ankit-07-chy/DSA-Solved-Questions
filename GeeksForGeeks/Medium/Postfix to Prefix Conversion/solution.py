class Solution:
    def postToPre(self, s):
        # Code here
        stack = []
        for char in s:
            if char not in ['+','-','*','/','^']:
                stack.append(char)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                ans = char+top2+top1
                stack.append(ans)
        return ''.join(stack)