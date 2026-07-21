class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(); s.sort()
        p = 0; i = 0
        while i < len(g):
            e = g[i]
            if p >= len(s):
                break
            if e <= s[p]:
                count += 1
                p += 1
            else:
                p += 1
                continue
            i += 1
        return count
            
