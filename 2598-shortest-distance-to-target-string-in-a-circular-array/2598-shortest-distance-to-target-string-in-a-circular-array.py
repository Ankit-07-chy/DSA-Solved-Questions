class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        result = float('inf')
        for i in range(n):
            if target == words[i]:
                straight_dist = abs(i-startIndex)
                circular_dist = n - straight_dist
                result = min(result,circular_dist,straight_dist)
        if result == float('inf'):
            return -1
        return result