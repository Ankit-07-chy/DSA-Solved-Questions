class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for _ in logs:
            if _ == '../':
                if stack:
                    stack.pop()
            elif _ == './':
                continue
            else:
                stack.append(_)
        return len(stack)