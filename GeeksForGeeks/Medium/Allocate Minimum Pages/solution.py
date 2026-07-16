class Solution:
    def findPages(self, arr, k):
        # code here
        
        if len(arr)<k : 
            return -1 
            
            
        def check(arr,page_to_read,students):
            # nonlocal mini
            n = len(arr)
            idx = 0
            
            allocated_students = 1
            curr_page = 0
            
            for page in arr:
                if page > page_to_read:
                    return False
                elif page+curr_page <= page_to_read:
                    
                    curr_page += page
                else:
                    allocated_students += 1
                    curr_page = page
            '''
            while idx < n:
                curr_page += arr[idx]
                
                if arr[idx]>page_to_read:
                    return False
                
                if curr_page > page_to_read:
                    curr_page = arr[idx]
                    allocated_students += 1
                idx += 1'''
                
            # if curr_students == 0:
                # mini = min(mini,page_to_read)
            return allocated_students <= students 
                
        
        
        low = max(arr); high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low+high)//2
            
            temp = check(arr,mid,k)
            
            if temp:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans