class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # no of char to change ==> len(substring) - max_freq_ele
        maxLen = 0; maxfreq = 0
        left = 0 ; right = 0
        heap = {}

        def findMaxFreq(heap):
            curr = 0
            for key,val in heap.items():
                curr = max(curr,val)

            return curr 

        for right in range(len(s)):
            if s[right] in heap:
                heap[s[right]] += 1
                maxfreq = max(maxfreq,heap[s[right]])
            elif s[right] not in heap:
                heap[s[right]] = 1
                maxfreq = max(maxfreq,heap[s[right]])

            while (right-left+1)-maxfreq >k:
                ele = heap[s[left]]
                heap[s[left]] -= 1
                if heap[s[left]] == 0:
                    heap.pop(s[left])
                # maxfreq = findMaxFreq(heap)
                left += 1

            if (right-left+1)-maxfreq<=k:
                maxLen = max(maxLen,right-left+1)

        return maxLen