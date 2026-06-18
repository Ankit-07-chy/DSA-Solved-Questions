class Solution:
    def infixtoPostfix(self, s):
        result = []
        stack = []
        
        def precedence(c):
            if c == '^':
                return 3
            if c == '*' or c == '/':
                return 2
            if c == '+' or c == '-':
                return 1
            return 0
        
        for _ in s:
            if _.isalpha() or _.isdigit():
                result.append(_)
            elif _ == '(':
                stack.append('(')
            elif _ == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                # For '^', only pop if stack top has HIGHER precedence (not equal)
                if _ == '^':
                    while stack and precedence(stack[-1]) > precedence(_) and stack[-1] != '(':
                        result.append(stack.pop())
                else:
                    # For other operators, pop if stack top has HIGHER OR EQUAL precedence
                    while stack and precedence(stack[-1]) >= precedence(_) and stack[-1] != '(':
                        result.append(stack.pop())
                stack.append(_)
        
        while stack:
            result.append(stack.pop())
        return ''.join(result)