from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = [[-1] * cols for i in range(rows)]

        """
        def find_nearest_0(i, j):  # here I am applying bfs, so it can help me here
            q = deque([])
            q.append([i, j, 0])  # this is for source node
            # make visited array here
            visited = [[False] * cols for i in range(rows)]
            visited[i][j] = True
            while q:
                i, j, d = q.popleft()
                adjNeighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for new_i, new_j in adjNeighbors:
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if mat[new_i][new_j] == 0:
                            return d + 1
                        elif mat[new_i][new_j] == 1 and visited[new_i][new_j] == False:
                            visited[new_i][new_j] = True
                            q.append([new_i, new_j, d + 1])

            return -1
        """

        def find_nearest(queue):
            # visited = [[-1] * cols for i in range(rows)]
            while queue:
                i, j = queue.popleft()

                adjList = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for new_i, new_j in adjList:
                    if (
                        0 <= new_i < rows
                        and 0 <= new_j < cols
                        and dist[new_i][new_j] == -1
                    ):
                        dist[new_i][new_j] = dist[i][j] + 1
                        queue.append([new_i, new_j])
                        #   visited[new_i][new_j] = 1

        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    # dis = find_nearest_0(i, j)
                    # dist[i][j] = dis
                    queue.append([i, j])
                    dist[i][j] = 0
        find_nearest(queue)
        return dist
