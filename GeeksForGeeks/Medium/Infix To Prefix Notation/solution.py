class Solution:
    def infixToPrefix(self, s):

        def precedence(op):
            if op == '^':
                return 3
            if op in "*/":
                return 2
            if op in "+-":
                return 1
            return 0

        # Reverse
        s = s[::-1]

        # Swap brackets
        temp = []
        for ch in s:
            if ch == '(':
                temp.append(')')
            elif ch == ')':
                temp.append('(')
            else:
                temp.append(ch)

        s = ''.join(temp)

        stack = []
        ans = []

        for ch in s:
            if ch.isalnum():
                ans.append(ch)

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':
                while stack and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()

            else:
                while stack and stack[-1] != '(':
                    if ch == '^':
                        if precedence(stack[-1]) >= precedence(ch):
                            ans.append(stack.pop())
                        else:
                            break
                    else:
                        if precedence(stack[-1]) > precedence(ch):
                            ans.append(stack.pop())
                        else:
                            break
                stack.append(ch)

        while stack:
            ans.append(stack.pop())

        return ''.join(ans[::-1])