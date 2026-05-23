class Solution:
    def check(self, nums: List[int]) -> bool:
        # find the position for Crack, Put all those Element in an Array from crack Index to end  and 0 to crack Index, then check for sorted into that array
        index_crack = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] >= nums[i]:
                continue
            else:
                index_crack = i+1
                break
        expected_array = []
        expected_array.extend(nums[index_crack:])
        expected_array.extend(nums[:index_crack])
        for i in range(0,n-1):
            if expected_array[i+1] < expected_array[i]:
                return False
        return True