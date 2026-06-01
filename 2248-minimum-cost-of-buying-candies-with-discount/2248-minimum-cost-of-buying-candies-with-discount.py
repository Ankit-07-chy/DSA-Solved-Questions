class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0; count = 1
        for c in cost:
            if count % 3 != 0:
                ans += c 
            count += 1
        return ans