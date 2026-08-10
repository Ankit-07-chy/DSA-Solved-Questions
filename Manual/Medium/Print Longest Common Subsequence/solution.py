def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    
    # first Find the DP for that

    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 +dp[i+1][j+1]

            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])

    # print(dp)
    # from This dp we know that dp[0][0] is giving maximum longest common subseq
    ans = []
    i = 0; j = 0
    while i<n and j < m:
        if s1[i] == s2[j]:
            ans.append(s2[j])
            i += 1
            j += 1
        
        elif dp[i][j+1] > dp[i+1][j]:
            j = j+1 
        else:
            i = i + 1
    return ''.join(ans)
            