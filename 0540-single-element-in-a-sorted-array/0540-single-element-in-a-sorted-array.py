# o(ln(n)) --> approach
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0; right = n-1
        if n == 1:
            return nums[0]

        while left < right:
            mid = (left+right)//2
            if mid % 2 == 1:
                mid -= 1   
            
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        exor operation for all --> o(n) in T.C. & o(1) --> S.C
        '''
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):  
            ans = ans^nums[i]
        return ans"""