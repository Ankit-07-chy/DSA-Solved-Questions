class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1

        x11,y11,x22,y22 = rec2 

        if x11 >= x2 or x22 <= x1:
            return False
        elif y11 >= y2 or y22 <= y1:
            return False

        return True
