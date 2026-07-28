class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # without KMP
        rev = s[::-1]
        n = len(s)
        for i in range(0,n):
            # substr compare
            if rev[i:] == s[0:n-i]:
                return rev[0:i]+s
        return rev + s