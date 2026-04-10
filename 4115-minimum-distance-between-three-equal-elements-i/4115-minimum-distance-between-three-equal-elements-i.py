class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def choose(arr):
            temp = float('inf')
            n = len(arr)
            for i in range(n-2):
                t1,t2,t3 = arr[i],arr[i+1],arr[i+2]
                temp = min(temp,abs(t1-t2)+abs(t2-t3)+abs(t3-t1))
            return temp
        freq= {} # element = [index]
        for idx,val in enumerate(nums):
            if val in freq:
                freq[val].append(idx)
            else:
                freq[val] = [idx]
        min_dist = float('inf')
        for key,val in freq.items():
            if len(val) >= 3:
                # choose
                curr = choose(val)
                min_dist = min(min_dist,curr)
        if min_dist == float('inf'):
            return -1
        return min_dist