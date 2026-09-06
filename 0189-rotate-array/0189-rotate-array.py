class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:] + nums[:-k]
        print(temp)
        for i in range(len(nums)):
            nums[i] = temp[i]
