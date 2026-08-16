class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+2) for i in range(n+2)]
        for idx in range(n-1,-1,-1):
            for prev_idx in range(idx-1,-2,-1):
                if prev_idx == -1:
                    pick = 1 + dp[idx+1][idx+1]
                else:
                    pick = 0
                    if nums[idx] > nums[prev_idx]:
                        pick = 1 + dp[idx+1][idx+1]
                    
                not_pick = dp[idx+1][prev_idx+1]

                dp[idx][prev_idx+1] = max(pick,not_pick)
        return dp[0][0]





"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[None]*(n+1) for i in range(n+1)]

        def f(idx,prev_idx):
            if idx >= n:
                return 0
            if dp[idx][prev_idx+1] == None:
                if prev_idx == -1:
                    pick = 1 + f(idx+1,idx)
                else:
                    pick = 0
                    if nums[idx]>nums[prev_idx]:
                        pick = 1 + f(idx+1,idx)
                
                not_pick = f(idx+1,prev_idx)
                dp[idx][prev_idx+1] = max(pick,not_pick)
            return dp[idx][prev_idx+1] 
        return f(0,-1)
        dp = [[None]*(n+1) for i in range(n+1)]

        def f(idx,prev_idx):
            if idx >= n:
                return 0
            if dp[idx][prev_idx+1] == None:
                if prev_idx == -1:
                    pick = 1 + f(idx+1,idx)
                else:
                    pick = 0
                    if nums[idx]>nums[prev_idx]:
                        pick = 1 + f(idx+1,idx)
                
                not_pick = f(idx+1,prev_idx)
                dp[idx][prev_idx+1] = max(pick,not_pick)
            return dp[idx][prev_idx+1] 
        return f(0,-1)
"""


'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def f(idx,prev_idx):
            if idx >= n :
                return 0
            if prev_idx == -1:
                pick = f(idx+1,idx) + 1
                not_pick = f(idx+1,prev_idx)
            else:
                pick = 0
                if nums[idx] > nums[prev_idx]:
                    pick = 1 + f(idx+1,idx)
                not_pick = f(idx+1,prev_idx)
            
            return max(pick,not_pick)
        return f(0,-1)
            
'''