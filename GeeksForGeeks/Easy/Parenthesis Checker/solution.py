class Solution:
    def isBalanced(self, s):
        # code here
        
        match = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        stack = []
        for char in s:
            # print(char)
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                temp = stack.pop()
                if match[temp] != char:
                    return False
        if len(stack) != 0:
            return False
        return True
                