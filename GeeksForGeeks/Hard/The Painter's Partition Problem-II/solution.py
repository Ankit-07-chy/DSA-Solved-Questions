class Solution:
    def minTime (self, arr, k):
        # code here
        low = max(arr)
        high = sum(arr); ans = high
        
        def find(arr,hrs,no_workers):
            curr_worker = 1
            curr_hr = 0
            for hr in arr:
                curr_hr += hr
                if curr_hr > hrs:
                    curr_hr = hr
                    curr_worker += 1
            return curr_worker <= no_workers
                
        
        
        while low <= high:
            mid = (low+high)//2
            
            t = find(arr,mid,k) # where mid is hrs, and k is the no of painters; this func will return true or false
            if t == True:
                high = mid - 1
                ans = mid
                
            else:
                low = mid + 1
                
        return ans