class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1 = None; count1 = 0; maj2 = None; count2 = 0; n = len(nums)
        for i in range(n):
            if nums[i] == maj1:
                count1 += 1
            elif nums[i] == maj2 :
                count2 += 1
            elif count1 == 0:
                count1 = 1
                maj1 = nums[i]
            elif count2 == 0:
                count2 = 1
                maj2 = nums[i]
            else:
                count1 -= 1
                count2 -= 1
        # verification
        count1 = 0; count2 = 0
        for num in nums:
            if num == maj1:
                count1 += 1
            if num == maj2 :
                count2 += 1
        if count1 > n//3 and count2 > n//3:
            return [maj1,maj2]
        elif count1 > n//3:
            return [maj1]
        elif count2 > n//3:
            return [maj2]
        return []

'''
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        result = []
        n = len(nums)
        for u,v in freq.items():
            if n//3 < v:
                result.append(u)
        return result
        '''