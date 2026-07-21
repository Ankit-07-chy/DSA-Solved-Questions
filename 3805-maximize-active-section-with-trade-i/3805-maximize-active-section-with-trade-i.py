class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        def count1s(string):
            count = 0
            for char in string:
                if char == '1':
                    count += 1
            return count
        activeCount = count1s(s)
        zeroBlock = []

        start = 0; i = 0; n = len(s)
        while i < n:
            if s[i] == '0':
                start = i

                while i < n and s[i] == '0':
                    i +=  1
                zeroBlock.append(i-start)
            else:
                i += 1
        ans = 0
        for i in range(0,len(zeroBlock)-1):
            ans = max(ans,zeroBlock[i]+zeroBlock[i+1])
        return ans+activeCount