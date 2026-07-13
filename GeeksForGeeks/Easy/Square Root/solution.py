class Solution:
    def floorSqrt(self, n): 
        # code here
        left = 0; right = n
        while left <= right:
            mid = (left+right)//2
            if mid**2 == n:
                return mid 
            elif mid**2 < n:
                left = mid+1 
            else:
                right = mid-1 
                
        return right