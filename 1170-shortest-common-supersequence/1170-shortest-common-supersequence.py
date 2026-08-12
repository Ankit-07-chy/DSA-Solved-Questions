class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # first Try to find length of longest common sequence

        '''
        def recursion(i,j):
            if s1[i] == s2[j]:
                return 1+recursion(i+1,j+1)
            else:
                return max(recursion(i+1,j),recursion(i,j+1))
        '''
        n = len(str1); m = len(str2)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        # print(dp)
        ans = []
        i = 0; j = 0
        while i < n and j < m:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1
            elif dp[i+1][j] > dp[i][j+1]:
                ans.append(str1[i])
                i += 1
            else:
                ans.append(str2[j])
                j += 1
        while i < n:
            ans.append(str1[i])
            i += 1
        while j < m:
            ans.append(str2[j])
            j+=1
        return ''.join(ans)
