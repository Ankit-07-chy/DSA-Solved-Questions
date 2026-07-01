class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        n = len(pre_exp)
        i = n-1
        while i > -1:
            char = pre_exp[i]
            if char in ['+','-','*','/','^']:
                t1 = stack.pop()
                t2 = stack.pop()
                ans = '('+t1+char+t2+')'
                stack.append(ans)
            else:
                stack.append(char)
            i -= 1
        return ''.join(stack)