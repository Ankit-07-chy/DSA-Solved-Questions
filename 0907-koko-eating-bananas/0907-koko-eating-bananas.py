import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0; high = max(piles)
        ans = high

        def find(arr,h,k):
            hr_curr = 0
            if k == 0:
                return False
            for a in arr:
                hr_curr += math.ceil(a/k)
            
            if hr_curr <= h:
                return True
            return False

        while low <= high:
            mid = (low+high)//2
            check = find(piles,h,mid)
            if check:
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans