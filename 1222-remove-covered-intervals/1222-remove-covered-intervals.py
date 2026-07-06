class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        start = -1
        end = -1
        count = 0
        for interval in intervals:
            if start<=interval[0]<=end and start<=interval[1]<=end:
                continue
            count += 1
            start = interval[0]; end = interval[1]

        return count