
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)
        dp = [[None]*(sum+1) for i in range(n+1)]
        
        def recursion(idx,curr_sum):
            if curr_sum == 0:
                return True
            elif idx >= n or curr_sum <0:
                return False
            
            
            
            if dp[idx][curr_sum] != None:
                return dp[idx][curr_sum]
            
            # pick
            pick = recursion(idx+1,curr_sum - arr[idx])
            not_pick = recursion(idx+1,curr_sum)
            dp[idx][curr_sum] = pick or not_pick
            
            return dp[idx][curr_sum]
        return recursion(0,sum)

'''
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)
        
        dp = {}
        
        def recursion(idx,curr_sum):
            if curr_sum == 0:
                return True
            if idx >= n:
                return False
            if (idx+1,curr_sum-arr[idx]) not in dp:
                dp[(idx+1,curr_sum-arr[idx])] = recursion(idx+1,curr_sum - arr[idx])
            pick = dp[(idx+1,curr_sum-arr[idx])]
            if (idx+1,curr_sum) not in dp:
                dp[(idx+1,curr_sum)] = recursion(idx+1,curr_sum)
            not_pick = dp[(idx+1,curr_sum)]
            return pick or not_pick
            
        return recursion(0,sum)
        
        # i = 0 ; j = 0
        # n = len(arr)
        # curr_sum = 0
        # for j in range(n):
        #     curr_sum += arr[j]
            
        #     if curr_sum == sum:
        #         return True
            
        #     while curr_sum > sum:
        #         curr_sum -= arr[i]
        #         i += 1
                
        # return False
        
        '''
            