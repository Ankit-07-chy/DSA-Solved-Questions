from typing import List
import functools

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Since costs is 1-indexed for steps 1 to n, 
        costs = [0] + costs  # Pad with 0 so costs[i] matches 1-based indexing if needed
        
        @functools.lru_cache(None)
        def fxn(idx: int) -> int:
            # If we reach step n, no more cost to add
            if idx == n:
                return 0
            # If we overshoot step n, return infinity
            if idx > n:
                return float('inf')
            
            min_cost = float('inf')
            
            # Try jumping 1, 2, or 3 steps ahead
            for step in range(1, 4):
                next_idx = idx + step
                if next_idx <= n:
                    # Cost formula: step_cost + costs[j] + (j - i)**2
                    jump_cost = costs[next_idx] + (next_idx - idx) ** 2
                    total_cost = jump_cost + fxn(next_idx)
                    min_cost = min(min_cost, total_cost)
                    
            return min_cost

        return fxn(0)