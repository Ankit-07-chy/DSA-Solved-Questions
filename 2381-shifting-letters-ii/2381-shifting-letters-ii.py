class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 1 -> forward and 0 means backward -> so i will do for backward as -1 means when ever I encounter 0 as val means I will change it to -1
        n = len(s)
        diff = [0]*len(s)

        for query in shifts:
            start = query[0]
            end = query[1]+1
            val = 1 if query[2] == 1 else -1

            diff[start] += val
            if end < n:
                diff[end] -= val
        for i in range(1,n):
            diff[i] += diff[i-1]
        # print(diff)

        s = list(s)
        for idx in range(n):
            change = diff[idx]
            char = s[idx]
            if change == 0:
                continue
            if change > 0:
                s[idx] = chr(((ord(s[idx]) - 97 + change) % 26) + 97)
            if change < 0:
                s[idx] = chr(((ord(s[idx]) - 97 + change) % 26) + 97)

        return ''.join(s)
            