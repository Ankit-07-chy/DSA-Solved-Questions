# sliding window and 2 pointer approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s); freq = {}
        l,r = 0,0; maxL = 0
        for r in range(n):
            if s[r] not in freq:
                freq[s[r]] = r
                maxL = max(maxL,r-l+1)
            else:
                prev = freq[s[r]]
                freq[s[r]] = r
                if prev >= l:
                    l = prev + 1
                else:
                    maxL = max(maxL,r-l+1)
        return maxL



# Brute Force Approach - O(n**2) T.C, O(n) S.C
'''
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
'''