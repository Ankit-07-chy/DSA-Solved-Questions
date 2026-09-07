class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        visited = [0]*(n+1)

        def solve(idx,stack):
            if len(stack)==k:
                ans.append(stack[:])
                return 
            for i in range(idx,n+1):
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)
                    solve(i+1,stack)
                    visited[i] = 0
                    stack.pop()

        solve(1,[])
        return ans