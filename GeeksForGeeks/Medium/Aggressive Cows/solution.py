class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        low = 1; high = arr[-1]
        ans = 1
        
        def check_can_place(arr,dist,cows):
            temp_cows = cows-1 # assumed first cows placed at arr[0]
            prev_placed_idx = 0
            
            for i in range(1,len(arr)):
                if arr[i]-arr[prev_placed_idx]>=dist and temp_cows:
                    temp_cows -= 1
                    prev_placed_idx = i 
            
            if temp_cows <= 0:
                return True
            return False
            
            
        
        
        while low <= high:
            mid = (low+high)//2
            
            temp = check_can_place(arr,mid,k)
            if temp == True:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans