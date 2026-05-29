class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = float('inf'); n = len(nums)
        for i in range(n):
            val = nums[i]
            curr = 0
            while val:
                curr += (val %10)
                val = val // 10
            mini = min(mini,curr)
        return mini
'''
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def find(number):
            number = str(number)
            curr = 0
            for _ in number:
                curr += int(_)
            return curr
        for idx,val in enumerate(nums):
            temp = val
            nums[idx] = find(temp)
        return min(nums)'''