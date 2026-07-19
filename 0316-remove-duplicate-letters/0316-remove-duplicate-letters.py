class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seq = {}
        for idx,char in enumerate(s):
            last_seq[char]=idx
        
        seen = set()
        stack = []
        for i,char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and last_seq[stack[-1]]>i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return ''.join(stack)

            