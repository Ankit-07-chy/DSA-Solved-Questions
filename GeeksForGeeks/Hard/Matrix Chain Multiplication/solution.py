from functools import cache
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        n = len(arr)
        @cache
        def f(i,j):
            if i == j:
                return 0
            mini = 10**9 
            for k in range(i,j):
                steps = f(i,k) + f(k+1,j) + arr[i-1]*arr[k]*arr[j]
                mini = min(mini,steps)
            return mini
        
        return f(1,n-1)