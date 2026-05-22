class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        def find_sequence(dp,idx,nums):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            if dp[idx] == -1:
                pick = find_sequence(dp,idx-2,nums) + nums[idx]
                not_pick = find_sequence(dp,idx-1,nums) + 0
                dp[idx] = max(pick,not_pick)
            return dp[idx]

        return find_sequence(dp,len(nums)-1,nums)
#Recursion Solution with TLE
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def find_all_subsequence(idx,nums): 
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            pick = nums[idx] + find_all_subsequence(idx-2,nums)
            not_pick = 0 + find_all_subsequence(idx-1,nums)
            return max(pick,not_pick)
        return find_all_subsequence(len(nums)-1,nums)
        '''