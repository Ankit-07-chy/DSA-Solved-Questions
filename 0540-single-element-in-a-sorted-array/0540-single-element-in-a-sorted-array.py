class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        exor operation for all --> o(n) in T.C. & o(1) --> S.C
        '''
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):
            ans = ans^nums[i]
        return ans