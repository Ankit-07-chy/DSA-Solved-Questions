class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        prev_mov = 'R'
        count_l = 0
        count_r = 0
        for i in range(n):
            if moves[i] == 'L':
                count_l += 1
            elif moves[i] == 'R':
                count_r += 1
        if count_r > count_l:
            choose = 'R'
        else:
            choose = 'L'
        count = 0
        for i in range(n):
            if moves[i] == 'L':
                count += 1
            elif moves[i] == 'R':
                count -= 1
            else:
                if choose == 'R':
                    count -= 1
                else:
                    count += 1
        return abs(count)