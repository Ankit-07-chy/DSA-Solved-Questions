class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) +1
        sumi =( n*(n+1)) / 2
        temp = sum(arr)
        return int(sumi - temp)