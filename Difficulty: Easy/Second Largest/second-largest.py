class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first_max = arr[0]
        second_max = -1
        n = len(arr)
        for i in range(1,n):
            if arr[i] > first_max:
                temp = first_max
                first_max = arr[i]
                second_max = temp
            elif arr[i] != first_max and arr[i] > second_max:
                second_max = arr[i]
                
        return second_max