class Solution:

    def unvisitedLeaves(self, arr, k):
        """code here"""
        visited = set()
        for i in range(len(arr)):
            t = 1
            while t*arr[i] <= k:
                visited.add(t*arr[i])
                t += 1
        return k - len(visited)