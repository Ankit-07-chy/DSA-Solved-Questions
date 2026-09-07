class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        visited = [0]*n

        def recursion(stack,visited):
            if len(stack) == n:
                ans.append(stack[:])
                return 
            for i in range(0,n):
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(nums[i])
                    recursion(stack,visited)
                    visited[i] = 0
                    stack.pop()
        recursion([],visited)
        return ans