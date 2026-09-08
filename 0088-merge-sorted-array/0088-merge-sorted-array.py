class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print(nums1,nums2)
        left = m-1; right = n-1; idx = n+m -1

        while left >= 0 and right >= 0:
            if nums1[left]>nums2[right]:
                nums1[idx] = nums1[left]
                left -= 1
                idx -= 1
            else:
                nums1[idx] = nums2[right]
                right -= 1
                idx -= 1

        while left >= 0:
            nums1[idx] = nums1[left]
            left -= 1
            idx -=1 
        while right >= 0:
            nums1[idx] = nums2[right]
            right -= 1
            idx -= 1
            

        