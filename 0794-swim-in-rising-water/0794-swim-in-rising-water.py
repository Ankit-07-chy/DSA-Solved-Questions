class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # just after seeing the question binary search coming to my mind and I am firstly movint in that direction only
        n = len(grid)

        def check(grid,water_height):
            visited = [[False]*n for i in range(n)]
            visited[0][0] = True
            from collections import deque
            queue = deque([])
            queue.append([0,0])
            
            while queue:
                i,j = queue.popleft()
                if i==n-1 and j == n-1:
                    return True
                idxs =[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for new_i,new_j in idxs:
                    if 0<=new_i<n and 0<=new_j<n and grid[new_i][new_j] <= water_height and visited[new_i][new_j] == False:
                        visited[new_i][new_j] = True
                        queue.append([new_i,new_j])
            return False


        low = 0; high = n**2 + 1
        # here low , high and mid is time ke respect hai
        ans = high
        while low <= high:
            mid = (low+high)//2

            if grid[0][0]>mid or grid[n-1][n-1]>mid:
                low = mid + 1
                continue

            temp = check(grid,mid)
            if temp:

                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
