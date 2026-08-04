class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for i in range(rows)]

        def dfs(i, j):
            idxs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for new_i, new_j in idxs:
                if (
                    0 <= new_i < rows
                    and 0 <= new_j < cols
                    and board[new_i][new_j] == "O"
                    and visited[new_i][new_j] == 0
                ):
                    visited[new_i][new_j] = 1
                    dfs(new_i, new_j)

        # going for the first row
        for i in range(cols):
            if board[0][i] == "O" and visited[0][i] == 0:
                visited[0][i] = 1
                dfs(0, i)
        # for last row
        for i in range(cols):
            if board[rows - 1][i] == "O" and visited[rows - 1][i] == 0:
                visited[rows - 1][i] = 1
                dfs(rows - 1, i)
        # for 1st column
        for i in range(rows):
            if board[i][0] == "O" and visited[i][0] == 0:
                visited[i][0] = 1
                dfs(i, 0)
        # for last column
        for i in range(rows):
            if board[i][cols - 1] == "O" and visited[i][cols - 1] == 0:
                visited[i][cols - 1] = 1
                dfs(i, cols - 1)

        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
