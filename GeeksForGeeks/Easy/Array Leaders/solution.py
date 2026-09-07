class Solution:
    def leaders(self, arr):
        # code here
        ans = [arr[-1]]
        n = len(arr)
        curr_max = arr[-1]
        for i in range(n-2,-1,-1):
            if arr[i]>=curr_max:
                ans.append(arr[i])
            curr_max = max(curr_max,arr[i])
        return ans[::-1]
        