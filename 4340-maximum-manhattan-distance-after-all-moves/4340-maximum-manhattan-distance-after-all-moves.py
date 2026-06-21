class Solution:
    def maxDistance(self, moves: str) -> int:
        countL,countR,countD,countU,count_ = 0,0,0,0,0

        for char in moves:
            if char == 'L':
                countL += 1
            elif char == 'R':
                countR += 1
            elif char == 'D':
                countD += 1
            elif char == 'U':
                countU += 1
            else:
                count_ += 1
        if countL > countR:
            _ = 'L'
        elif countR > countL:
            _ = 'R'
        elif countU > countD:
            _ = 'U'
        elif countD > countU:
            _ = 'D'
        else:
            _ = 'L'

        leftCount = 0; upCount = 0
        for char in moves:
            if char == 'L':
                leftCount -= 1
            elif char == 'R':
                leftCount += 1
            elif char == 'U':
                upCount += 1
            elif char == 'D':
                upCount -= 1
            else:
                if _ == 'L':
                    leftCount -= 1
                elif _ == 'R':
                    leftCount += 1
                elif _ == 'U':
                    upCount += 1
                else:
                    upCount -= 1
        return abs(leftCount) + abs(upCount)