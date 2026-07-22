import math
inf = math.inf
class Solution:
    def maxMeetings(self, s, f):
        # code here
        list1 = []
        for idx in range(len(s)):
            list1.append([idx,s[idx],f[idx]])
            
        list1.sort(key=lambda x:x[-1])
        ans = []
        # print(list1)
        prev_start = -1; prev_end = -inf
        for original_idx, start, end in list1:
            # 3. Check for non-overlap
            if start > prev_end:
                ans.append(original_idx + 1) # Convert to 1-based index
                prev_end = end 
        return sorted(ans)
            