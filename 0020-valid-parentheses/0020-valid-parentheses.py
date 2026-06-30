class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char in match and not stack:
                return False
            elif char in match and stack:
                curr = char
                top = stack[-1]
                if top != match[curr]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True