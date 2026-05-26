class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # event 2 start in event 1 [start,end] or event1 start in event2 [start,end]
        start1 = int(event1[0][:2])*60 + int(event1[0][3:])
        end1 = int(event1[1][:2])*60 + int(event1[1][3:])

        start2 = int(event2[0][:2])*60 + int(event2[0][3:])
        end2 = int(event2[1][:2])*60 + int(event2[1][3:])

        if start1<=start2<=end1 or start2<=start1<=end2:
            return True
        return False
        '''
        hr2a = int(event2[0][:2]); hr2b = int(event2[1][:2])
        hr1a = int(event1[0][:2]); hr1b = int(event1[1][:2])
        min1a = int(event1[0][3:]); min1b = int(event1[1][3:])
        min2a = int(event2[0][3:]); min2b = int(event2[1][3:])

        t1a = hr1a*60 + min1a; t2a = hr1b*60 + min1b
        t1b = hr2a*60 + min2a; t2b = hr2b*60 + min2b
        # check event2 in b/w event1 start and end
        if t1b<t1a<t2b or t1a<t2a<t1b:
            return False
        return True'''
