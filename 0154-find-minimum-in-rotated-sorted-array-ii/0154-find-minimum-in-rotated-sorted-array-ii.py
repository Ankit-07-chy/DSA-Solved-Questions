class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        left = 0; right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            temp = nums[mid]

            if nums[left] < nums[mid]:
                ans = min(ans,nums[left])
                left = mid + 1
            elif nums[mid] < nums[right]:
                ans = min(ans,nums[mid])
                right = mid - 1
            else:
                ans = min(ans,nums[left],nums[right])
                left += 1
                right -= 1
                
        return ans