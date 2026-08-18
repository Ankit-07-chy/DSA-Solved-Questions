from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # freq[x] = number of windows of size k containing x
        freq = {}

        # First window
        window = set(nums[:k])
        for x in window:
            freq[x] = freq.get(x, 0) + 1

        # Remaining windows
        for i in range(k, n):
            window = set(nums[i - k + 1:i + 1])

            for x in window:
                freq[x] = freq.get(x, 0) + 1

        ans = -1
        for x, count in freq.items():
            if count == 1:
                ans = max(ans, x)

        return ans