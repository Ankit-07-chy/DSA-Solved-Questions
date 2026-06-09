class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = 0; n = len(nums)
        dp = [[None]*(total+1) for i in range(n)]
        def isSubset(total,target,idx):
            if total == target:
                return True
            if idx == 0:
                return target == total
            if target < 0:
                return False
            if dp[idx][target] == None:
                pick = isSubset(total-nums[idx],target+nums[idx],idx-1)
                not_pick = isSubset(total,target,idx-1)
                dp[idx][target] = pick or not_pick
            return dp[idx][target]
        return isSubset(total,0,n-1)
# This is Recursion approach will give TLE
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = 0; n = len(nums)
        def isSubset(total,target,idx):
            if total == target:
                return True
            if idx == 0:
                return target == total
            pick = isSubset(total-nums[idx],target+nums[idx],idx-1)
            not_pick = isSubset(total,target,idx-1)
            return pick or not_pick
        return isSubset(total,0,n-1)'''