class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def helper(start, end):
            if start == end:
                return nums[start]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            # Choose the start or the end, and take the maximum difference possible
            pick_start = nums[start] - helper(start + 1, end)
            pick_end = nums[end] - helper(start, end - 1)
            
            memo[(start, end)] = max(pick_start, pick_end)
            return memo[(start, end)]
        
        # If Player 1's net score difference is >= 0, Player 1 wins or ties.
        return helper(0, len(nums) - 1) >= 0