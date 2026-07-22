class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[1]-x[0],x[0]))
        print(intervals)
        count = 0
        prev_end = -inf
        for u,v in intervals:
            if u < prev_end:
                count += 1
            elif u >= prev_end :
                prev_end = v
        return count