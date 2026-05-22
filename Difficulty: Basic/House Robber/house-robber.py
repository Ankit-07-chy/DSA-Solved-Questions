#User function Template for python3
class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        num = N//2
        if N % 2 != 0:
            num += 1
        return num*K
'''
## This is using DP approach
class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        arr = [K]*N
        dp = [-1]*(N+1)
        def find_seq(arr,idx,dp):
            if idx == 0:
                return arr[idx]
            if idx < 0:
                return 0
            if dp[idx] == -1:
                pick = arr[idx] + find_seq(arr,idx-2,dp)
                not_pick = 0 + find_seq(arr,idx-1,dp)
                dp[idx] = max(pick,not_pick)
            return dp[idx]
        return find_seq(arr,N-1,dp)
        '''