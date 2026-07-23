class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        count = 0
        ans = 0
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(arr) and ptr2 < len(dep):
            if arr[ptr1]<=dep[ptr2]:
                count += 1
                ans = max(ans,count)
                ptr1 += 1
            
            else:
                #ptr1 += 1
                ptr2 += 1
                count -= 1
                #ans = ans+1
                
        return ans