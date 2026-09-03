class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        n = len(arr)
        dp = [[0]*(k+2) for i in range(n+2)]
        # first put base case in dp 
        for i in range(0,n+1):
            dp[i][0] = 1
       
        
        for idx in range(n-1,-1,-1):
            for target in range(1,k+1):
                pick = 0
                if target - arr[idx] >= 0:
                    pick = dp[idx+1][target-arr[idx]]
                not_pick = dp[idx+1][target]
                dp[idx][target] = pick + not_pick
                
        
        return dp[0][k] > 0

'''
class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        n = len(arr)
        
        dp = [[None]*(k+1) for i in range(n+1)]
        
        
        def recursion(idx,target):
            
            if target == 0:
                return 1
            elif idx == n and target != 0:
                return 0
            else:
                if dp[idx][target] == None:
                    pick = 0
                    if target-arr[idx] >= 0:
                        pick = recursion(idx+1,target-arr[idx])
                    not_pick = recursion(idx+1,target)
                    dp[idx][target] = pick + not_pick
                return dp[idx][target]
        return recursion(0,k) > 0
        
'''