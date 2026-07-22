class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # inplace changee have to do
        intervals.sort(key=lambda x:x[0])
        si = newInterval[0]; ei = newInterval[1]

        def merge(intervals: List[List[int]]) -> List[List[int]]:
            if len(intervals) == 0 or len(intervals) == 1:
                return intervals
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

        if not intervals:
            return [newInterval]

        intervals.append([newInterval[0],newInterval[1]])
        '''
        for idx in range(len(intervals)):
            u = intervals[idx][0]
            v = intervals[idx][1]

            if u<=si<=v:
                intervals[idx][1] = max(ei,v)
                break
            if si<=u<=ei:
                intervals[idx][0] = min(si,u)
                break
            intervals.append()
        print(intervals)'''
        return merge(intervals)
        
        # return intervals
