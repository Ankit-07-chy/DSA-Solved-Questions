class Solution:
    def maxMeetings(self, s: list[int], f: list[int]) -> list[int]:
        # code here
        start = s; end = f
        
        lists = []
        n = len(start)
        for i in range(n):
            curr = [start[i],end[i],i+1]
            lists.append(curr)
        lists.sort(key = lambda x: x[1])

        count = 0
        index = []
        freeTime = -1
        for i in range(n):
            curr = lists[i]
            if curr[0]>freeTime:
                freeTime = curr[1]
                count += 1
                index.append(curr[-1])
        return sorted(index)