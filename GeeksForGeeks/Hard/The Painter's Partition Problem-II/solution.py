class Solution:
    def minTime (self, arr, k):
        # code here
        
        low = min(arr); high = sum(arr)
        ans = high
        
        def check(arr,work_to_done_a_painter,total_painters):
            curr_painter = 1 
            curr_day = 0
            for day in arr:
                if day > work_to_done_a_painter:
                    return False
                elif curr_day + day <= work_to_done_a_painter:
                    curr_day += day
                else:
                    curr_day = day
                    curr_painter += 1
                    
            return curr_painter <= total_painters
        
        
        while low <= high :
            mid = (low+high)//2
            
            if check(arr,mid,k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans