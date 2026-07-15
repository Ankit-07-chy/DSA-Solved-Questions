class Solution:
    def lis(self, arr):
        # code here
        length = 0
        temp = []
        
        def lower_bound(array,ele) -> int:
            low = 0; high = len(array)-1
            idx = high; final = array[-1]
            
            while low <= high:
                mid = (low+high)//2
                if array[mid] == ele:
                    return mid 
                elif array[mid]>ele:
                    idx = mid
                    final = array[mid]
                    high = mid - 1
                else:
                    low = mid + 1
            return idx 
        
        
        for ele in arr:
            if not temp:
                length+=1
                temp.append(ele)
            elif ele>temp[-1]:
                length+=1
                temp.append(ele)
            else:
                idx = lower_bound(temp,ele)
                temp[idx] = ele
                
        return length
        
