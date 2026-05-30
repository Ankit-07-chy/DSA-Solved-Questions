class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k%n
        def reverse(arr,left,right):
            while left < right:
                arr[left],arr[right]=arr[right],arr[left]
                left += 1
                right -= 1
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

# it will give TLE as O(n*K)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        for i in range(k):
            last = nums[-1]
            for j in range(n-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = last
"""

# using extra space - But I assume there should Be a mathematical way by which we can easily do it
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        arr = []
        for i in range(n-k,n):
            arr.append(nums[i])
        for i in range(0,n-k):
            arr.append(nums[i])
        print(arr)
        for i in range(n):
            nums[i] = arr[i]'''