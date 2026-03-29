class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        first = 0; last = n-1
        while first<=last:
            if s[first] == s[last]:
                return first
            first += 1
            last -= 1
        return -1