class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        repeat =-1
        sumi = 0
        for i in range(len(arr)):
            if i>0 and arr[i] == arr[i-1]:
                repeat = arr[i]
            sumi += arr[i]
            
        sumi = sumi - repeat
        total_sum = (n*(n+1))/2
        miss = int(total_sum - sumi)
        return [repeat,miss]
            
        