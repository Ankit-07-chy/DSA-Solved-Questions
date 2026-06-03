# Optimal Approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0; fast = 0
        while True:
            slow = nums[slow]; fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
# better approach
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for u in nums:
            if u in freq:
                freq[u] += 1
            else:
                freq[u] = 1
        for key,val in freq.items():
            if val >= 2:
                return key'''