from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')':
            return False

        # A valid path has even length.
        if (m + n - 1) % 2 != 0:
            return False

        @cache
        def recursion(row, col, balance):

            # Invalid balance
            if balance < 0:
                return False

            # Out of bounds
            if row >= m or col >= n:
                return False

            # Update balance for current cell
            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            # We reached destination
            if row == m - 1 and col == n - 1:
                return balance == 0

            # Move down or right
            return (
                recursion(row + 1, col, balance)
                or
                recursion(row, col + 1, balance)
            )

        return recursion(0, 0, 0)