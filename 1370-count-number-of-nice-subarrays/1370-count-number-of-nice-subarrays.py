class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def findSubarray(arr,k):
            if k <0:
                return 0
            left = 0; right = 0
            count = 0; odd_count = 0
            for right in range(0,len(nums)):
                if nums[right]%2 == 1:
                    odd_count += 1

                while odd_count > k:
                    if nums[left]%2==1:
                        odd_count -= 1
                    left += 1

                count += right-left + 1
            return count
        return findSubarray(nums,k)-findSubarray(nums,k-1)
