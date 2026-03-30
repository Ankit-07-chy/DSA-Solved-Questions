class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        start = 0; end = 0
        minL = float('inf')
        for u in strs:
            minL = min(minL,len(u))

        n = len(strs)
        
        for i in range(minL):
            currChar = strs[0][i]
            for j in range(n):
                if strs[j][i]!=currChar:
                    return strs[0][:end]
            end += 1
        # s = strs[0]
        return strs[0][:minL]