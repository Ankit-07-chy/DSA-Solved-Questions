class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        for char in postfix:
            if char not in ['+','-','*','/','^']:
                stack.append(char)
            else:
                prev2 = stack.pop()
                prev1 = stack.pop()
                ans = '('+prev1+char+prev2+')'
                stack.append(ans)
        return ''.join(stack)