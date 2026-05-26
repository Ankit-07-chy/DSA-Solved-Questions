class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        max_len = 0
        for i in range(n):
            curr = 0; seen = set()
            for j in range(i,n):
                if s[j] not in seen:
                    seen.add(s[j])
                    curr = j - i + 1
                else:
                    break
            max_len = max(curr,max_len)
        return max_len
