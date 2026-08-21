class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            rem = prefix % k
            if rem < 0:
                rem += k

            count += freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return count