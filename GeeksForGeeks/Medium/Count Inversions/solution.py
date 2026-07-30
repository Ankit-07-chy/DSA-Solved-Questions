class Solution:
    def inversionCount(self, arr):
        # code here
        count = 0
        
        def merge(arr,left,mid,right):
            nonlocal count
            i = left; j = mid + 1
            temp = []
            
            while i <= mid and j <= right:
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    count += (mid - i + 1)
                    temp.append(arr[j])
                    j += 1
                    
            while i<=mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
                
            for k in range(len(temp)):
                arr[left+k] = temp[k]
                
                
        
        def divide(arr,left,right):
            if left >= right:
                return
            
            mid = (left+right)//2
            divide(arr,left,mid)
            divide(arr,mid+1,right)
            
            merge(arr,left,mid,right)
        
        divide(arr,0,len(arr)-1)
        return count
            
            

'''
class Solution:
    def inversionCount(self, arr):
        # code here
        
        n = len(arr)
        count = 0
        for i in range(0,n):
            for j in range(i+1,n): # i+1, ensures my j is ahead of i
                if arr[i]>arr[j]:
                    count += 1
        return count
        # t.c. -> o(n**2) , s.c. -> o(1)'''