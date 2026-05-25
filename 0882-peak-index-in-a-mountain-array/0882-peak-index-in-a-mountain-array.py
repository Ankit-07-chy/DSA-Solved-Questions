class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0; right = n-1
        while left <= right:
            mid = (left + right)//2
            mid_prev = mid-1
            mid_next = mid+1
            if 0<=mid_prev<=n-1 and 0<=mid_next<=n-1:
                if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                    return mid
            if arr[mid]>arr[mid+1]:
                right = mid
            if arr[mid]<arr[mid+1]:
                left = mid
                