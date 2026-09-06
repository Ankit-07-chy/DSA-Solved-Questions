class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        long = 0
        freq = {0:-1}
        pref = 0
        n = len(arr)
        for i in range(n):
            pref += arr[i]
            remain = pref - k
            if remain in freq:
                long = max(long,i-freq[remain])
            if pref not in freq:
                freq[pref] = i
        return long
                