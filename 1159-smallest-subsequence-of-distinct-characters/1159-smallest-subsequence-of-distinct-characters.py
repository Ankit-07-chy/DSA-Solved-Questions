class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store last occurrence of each character
        last_seq = {}
        for idx, char in enumerate(s):
            last_seq[char] = idx
        
        stack = []
        seen = set()  # Track characters already in stack
        
        for i, char in enumerate(s):
            # Skip if character already in stack
            if char in seen:
                continue
            
            # While stack not empty AND current char is smaller than stack top
            # AND the stack top appears later in the string
            while stack and char < stack[-1] and last_seq[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            
            # Add current character
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)