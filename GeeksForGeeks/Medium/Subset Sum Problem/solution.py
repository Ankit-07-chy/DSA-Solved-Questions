class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[None] * (sum + 1) for _ in range(n)]
        
        def isSubset(idx,target):
            if target == 0:
                return True
            if idx == 0:
                return target == arr[0]
            if target < 0:
                return False
            if dp[idx][target] == None:
                
                pick = isSubset(idx-1,target-arr[idx])
                not_pick = isSubset(idx-1,target)
                dp[idx][target] = (pick or not_pick)
            return dp[idx][target]
        return isSubset(n-1,sum)


# This code will give TLE
'''
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        def isSubset(idx,arr,target):
            if idx >= n and target == 0:
                return True
            if idx >= n and target != 0:
                return False
            if target == 0:
                return True
            if target < 0:
                return False
            # pick
            one = isSubset(idx+1,arr,target-arr[idx])
            #not pick
            two = isSubset(idx+1,arr,target)
            return one or two
        return isSubset(0,arr,sum)
        '''