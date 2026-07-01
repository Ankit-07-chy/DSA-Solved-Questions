class Solution:
    def preToPost(self, s):
        # Code here
        stack = []
        s = s[::-1]
        for char in s:
            if char not in ['+','-','*','/','^']:
                stack.append(char)
            else:
                top1 = ''
                if stack:
                    top1 = stack.pop()
                top2 = ''
                if stack:
                    top2 = stack.pop()
                ans = top1+top2+char
                stack.append(ans)
        return ''.join(stack)