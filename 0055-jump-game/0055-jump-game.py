class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxVal = 0
        if len(nums)==1:
            return True
        for idx,val in enumerate(nums):
            if idx <= maxVal:
                maxVal = max(maxVal,idx+val)
            else:
                return False
        return maxVal >= len(nums)-1


'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = [False]*n
        reach[0]= True
        for i in range(n):
            if reach[i]:
                for j in range(min(n,i+nums[i]+1)):
                    reach[j] = True
        return reach[n-1]'''