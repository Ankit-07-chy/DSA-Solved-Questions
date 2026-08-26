class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        i = 0; ones_count = 0; maxLen = 10**8

        for j in range(len(s)):
            if s[j] == '1':
                ones_count += 1
            
            while ones_count > k:
                if s[i] == '1':
                    ones_count -= 1
                i += 1
            while i < j and s[i] == '0':
                i += 1

            if ones_count == k:
                if j - i + 1 < maxLen :
                    maxLen = j - i + 1
                    ans = s[i:j+1]
                elif j - i + 1 == maxLen:
                    ans = min(ans,s[i:j+1])
        return ans
