class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))

        n = len(words)
        dp = [1]*n
        max_len = 1

        def check(str1,str2):
            count = 0
            n1 = len(str1); n2 = len(str2)
            if n1 + 1 != n2 :
                return False
            i = 0; j = 0
            while i < n1 and j < n2:
                if str1[i] == str2[j]:
                    i += 1; j += 1
                else:
                    j += 1 
                    count += 1
            if i < n1:
                count += 1
            if j < n2:
                count += 1
            return count <= 1

        for i in range(0,n):
            for prev in range(0,i):
                if check(words[prev],words[i]) and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
            
            # max_len = max(max_len,dp[i])
        return max(dp)