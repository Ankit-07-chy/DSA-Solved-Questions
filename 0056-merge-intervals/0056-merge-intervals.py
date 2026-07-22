class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        new_array = []
        new_array.append(intervals[0])

        for i in range(1,len(intervals)):
            si = intervals[i][0]; ei = intervals[i][1]
            if new_array[-1][-1]<si: # no matching
                new_array.append([si,ei])
            elif new_array[-1][-1] == si: # match + just boundary touch
                u,v = new_array.pop()
                v = ei
                new_array.append([u,v])
            else:
                u,v = new_array.pop()
                u = min(u,si)
                v = max(v,ei)
                new_array.append([u,v])

        return new_array
                