class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = []
        ans.append(intervals[0])
        busy = intervals[0][1]
        n = len(intervals)

        for i in range(1,n):
            if intervals[i][0] > busy:
                busy = intervals[i][1]
                ans.append(intervals[i])
            else:
                temp = ans.pop()
                start = min(temp[0],intervals[i][0])
                end = max(temp[1],intervals[i][1])
                busy = end
                ans.append([start,end])
        return ans
        