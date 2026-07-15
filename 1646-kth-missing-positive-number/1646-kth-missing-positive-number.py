class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # Brute force
        for i in arr:
            if i <= k:
                k += 1
        return k