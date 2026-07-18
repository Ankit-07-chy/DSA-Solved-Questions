class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0; right_sum = 0
        for i in range(k):
            left_sum += cardPoints[i]
        ans = left_sum

        n = len(cardPoints)
        mid = k-1; right = n -1

        while mid >= 0:
            left_sum -= cardPoints[mid]
            mid -= 1
            right_sum += cardPoints[right]
            right -= 1
            ans = max(ans,left_sum + right_sum)

        return ans