class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0; right = n-1
        ans = float('inf')
        while left <= right:
            if nums[left]<=nums[right]:
                ans = min(ans,nums[left])
                break
            mid = (left+right)//2

            # here we will find 2 things , 1 sorted part , 2nd not sorted part
            if nums[left]<=nums[mid]: # means left part is sorted
                ans = min(ans,nums[left])
                # now search in right part is any small possible than this
                left = mid + 1
            else:
                ans = min(ans,nums[mid])
                right = mid - 1
            
        return ans

        """

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

        """