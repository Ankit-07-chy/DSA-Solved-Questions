class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        '''
        1 indexed array, -> distributed nums to arr1 and arr2, nums[1] to arr1 and nums[2] to arr[2] and afterwards ith ops, 
        if last element of arr1 is greater than the last element of arr2 , append nums[i] to arr1.
        reslt = concat(arr1,arr2)

        '''
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        i = 2; n = len(nums)
        while i < n:
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            
            i += 1
        return arr1 + arr2