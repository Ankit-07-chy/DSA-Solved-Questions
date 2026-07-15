class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            missed = arr[mid] - (mid+1)

            if missed < k:
                low = mid + 1
            else:
                high = mid - 1
        miss = arr[high] - (high+1)
        return low + k



# Brute force
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # Brute force
        for i in arr:
            if i <= k:
                k += 1
        return k
        '''