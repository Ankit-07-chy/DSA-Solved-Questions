class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = len(s)
        for i in range(n-1):
            a = int(s[i]); b = int(s[i+1])
            if abs(a-b) > 2:
                return False
        return True