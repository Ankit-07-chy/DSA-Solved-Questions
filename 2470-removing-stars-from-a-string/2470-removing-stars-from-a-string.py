class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '*' and stack:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)