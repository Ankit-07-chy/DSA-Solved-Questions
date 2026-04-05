class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # For Left and right assign +1 and -1 similarly for up and down assign +1 and -1 but in different variable
        row = 0; col = 0
        n_rows = len(moves)
        for i in range(n_rows):
            if moves[i] == 'L':
                row += 1
            if moves[i] == 'R':
                row -= 1
            if moves[i] == 'U':
                col -= 1
            if moves[i] == 'D':
                col += 1
        if row != 0 or col != 0 :
            return False
        return True
