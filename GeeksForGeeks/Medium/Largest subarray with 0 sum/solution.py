class Solution:
    def maxLength(self, arr):
        # code here
        hashMap = {0:-1}
        maxLen = 0
        n = len(arr)
        prefix = 0
        
        for i in range(n):
            prefix += arr[i]
            
            if prefix in hashMap:
                maxLen = max(maxLen,i-hashMap[prefix])
            else:
                hashMap[prefix] = i
        return maxLen