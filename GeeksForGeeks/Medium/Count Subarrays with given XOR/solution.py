class Solution:
    def subarrayXor(self, arr, m):
        # code here
        hashMap = {0:1}
        
        count = 0; pref = 0
        for i in range(len(arr)):
            pref = pref ^ arr[i]
            remain = m ^ pref
            if remain in hashMap:
                count += hashMap[remain]
            hashMap[pref] = hashMap.get(pref,0) + 1
        return count