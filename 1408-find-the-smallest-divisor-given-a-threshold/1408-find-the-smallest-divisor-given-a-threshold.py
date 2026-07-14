import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 0; high = max(nums); ans = max(nums)
        
        def check(nums, divisor, threshold):
            result = 0
            for num in nums:
                if divisor:
                    result += math.ceil(num/divisor)
            if result <= threshold and result != 0:
                return True
            return False


        while low <= high:
            mid = (low+high)//2
            t = check(nums, mid, threshold)
            if t == True:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
