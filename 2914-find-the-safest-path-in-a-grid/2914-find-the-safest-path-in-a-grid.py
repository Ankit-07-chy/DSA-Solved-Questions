from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid) # for finding length
        
        def check_possibility(dist_mat,max_dist,i,j,dest_i,dest_j):
            queue = deque([])
            queue.append([i,j])
            visited = [[False]*n for _ in range(n)]
            visited[0][0] = True

            while queue:
                curr_i,curr_j = queue.popleft()
                if curr_i == dest_i and curr_j == dest_j:
                    return True
                idxs = [(curr_i+1,curr_j),(curr_i-1,curr_j),(curr_i,curr_j+1),(curr_i,curr_j-1)]
                for new_i,new_j in idxs:
                    if 0<=new_i<n and 0<=new_j<n and dist_mat[new_i][new_j] >= max_dist and visited[new_i][new_j] == False:
                        queue.append([new_i,new_j])
                        visited[new_i][new_j] = True
            return False

        dist_matrix = [[-1]*n for i in range(n)]
        visited = [[False]*n for i in range(n)]
        # for multisource bfs I am taking queue
        queue = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # chor pakda gya
                    queue.append([i,j])
                    dist_matrix[i][j] = 0
                    visited[i][j] = True

        # apply now bfs(MS) on the queue
        while queue:
            i,j = queue.popleft()
            idxs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for new_i,new_j in idxs:
                if 0<=new_i<n and 0<=new_j<n and visited[new_i][new_j] == False:
                    dist_matrix[new_i][new_j] = dist_matrix[i][j] + 1
                    queue.append([new_i,new_j])
                    visited[new_i][new_j] = True
        # print(dist_matrix)
        # the case where the thief either in source or destination point
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        low = 0; high = 800 # this is the maximum distance that can happend b/w theif and the person
        source_i = 0; source_j = 0; dest_i = n-1; dest_j = n-1
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if dist_matrix[source_i][source_j] < mid or dist_matrix[dest_i][dest_j] < mid:
                high = mid -1
                continue
            if dist_matrix[source_i][source_j] >= mid and dist_matrix[dest_i][dest_j]>=mid:
                temp = check_possibility(dist_matrix,mid,source_i,source_j,dest_i,dest_j)
                print(temp)
                if temp:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

        return ans



        '''

        def check_possibility(dist_mat,max_dist,source_i,source_j,dest_i,dest_j):
            if dist_mat[source_i][source_j] > max_dist:
                return False
            if source_i == dest_i and source_j == dest_j:
                return True
            # possible idxs
            idxs = [(source_i+1,source_j),(source_i-1,source_j),(source_i,source_j+1),(source_i,source_j-1)]

            possibility = set()
            for new_i,new_j in idxs:
                if 0<=new_i<n and 0<=new_j < n and dist_mat[new_i][new_j]<=max_dist:
                    possibility.add(check_possibility(dist_mat,max_dist,new_i,new_j,dest_i,dest_j))
                
            return True if True in possibility else False
        # here is recursion approach bt we can memize it too
        '''