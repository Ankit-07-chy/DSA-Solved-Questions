class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        size = nums[-1] 
        diff = [0]*(size+2)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
            start = max(num - k,0)
            end = min( num + k , nums[-1])
            val = 1
            diff[start] += val
            if end + 1 < size:
                diff[end+1] -= val
        for i in range(1,size+2):
            diff[i] += diff[i-1]
        ans = 0
        for i in range(0,size+1):
            actual_freq = freq.get(i,0)
            can_be = diff[i]

            change = can_be - actual_freq
            ans = max(ans,actual_freq + min(change,numOperations))
        return ans