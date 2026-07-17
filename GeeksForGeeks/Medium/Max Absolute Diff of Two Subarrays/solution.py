class Solution:
    def maxDiffSubArrays(self, arr):
        # code here
        
        n = len(arr)
        leftMax = [0]*n
        leftMin = [0]*n 
        rightMax = [0]*n
        rightMin = [0]*n
        
        leftMax[0] = arr[0]
        # find leftMax 
        curr = arr[0]
        maxi = arr[0]
        for i in range(1,n):
            if curr+arr[i]<arr[i]:
                curr = arr[i]
            else:
                curr += arr[i]
            maxi = max(maxi,curr)
            leftMax[i] = maxi
        
        
        leftMin[0] = arr[0]
        # find leftMin
        curr = arr[0]
        mini = arr[0]
        for i in range(1,n):
            if curr+arr[i]>arr[i]:
                curr = arr[i]
            else:
                curr += arr[i]
            mini = min(mini,curr)
            leftMin[i] = mini
            
        rightMax[-1] = arr[-1]
        # find rightMax
        curr = arr[-1]
        maxi = arr[-1]
        for i in range(n-2,-1,-1):
            if curr + arr[i]<arr[i]:
                curr = arr[i]
            else:
                curr += arr[i]
            maxi = max(maxi,curr)
            rightMax[i] = maxi
        
        rightMin[-1] = arr[-1]
        # find rightMin
        curr = arr[-1]
        mini = arr[-1]
        for i in range(n-2,-1,-1):
            if curr + arr[i]>arr[i]:
                curr = arr[i]
            else:
                curr += arr[i]
            mini = min(mini,curr)
            rightMin[i] = mini
            
        
        ans = float("-inf")

        for i in range(n-1):
            ans = max(ans,
                      abs(leftMax[i] - rightMin[i+1]),
                      abs(leftMin[i] - rightMax[i+1]))
        return ans
"""
class Solution:
    def maxDiffSubArrays(self, arr):
        # code here
        
        # here the main problem given to the question is non-overlaping
        ''' using kadan's algo make a subarray which has maximum +ve, 
        and using same make a subarray with max but -ve, and 
        then give absolute diff b/w them '''
        
        maxi = arr[0]
        curr = arr[0]
        for i in range(1,len(arr)):
            if curr + arr[i] < 0:
                curr = arr[i]
            else:
                curr += arr[i]
            maxi = max(maxi,curr)
        # print(maxi) --> I am succesfully able to find the maximum
        
        mini = arr[0]
        curr = arr[0]
        
        for i in range(1,len(arr)):
            if curr+arr[i]>=0:
                curr = arr[i]
            else:
                curr += arr[i]
            mini = min(mini,curr)
            
        # print(mini,maxi)
        return maxi - mini
        """