class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 1:
                j = i
                while j < n and nums[j] == 1:
                    j += 1
                
                maxi = max(maxi,j-i)
                i = j+1
            else:
                i += 1
        return maxi