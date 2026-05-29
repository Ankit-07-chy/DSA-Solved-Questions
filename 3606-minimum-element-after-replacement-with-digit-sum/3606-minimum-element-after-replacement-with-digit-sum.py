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
        return min(nums)