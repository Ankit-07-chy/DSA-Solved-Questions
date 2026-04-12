import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a = sides[0]; b = sides[1]; c = sides[2]
        if a+b <= c or b+c<=a or c+a <= b:
            return []
            
        angle = [0]*3
        angle[0] = (b**2 + c**2 - a**2)/(2.0*b*c)
        angle[1] = (a**2 + c**2 - b**2)/(2.0*a*c)
        angle[2] = (b**2 + a**2 - c**2)/(2.0*b*a)
        angle[0] = math.acos(max(-1.0, min(1.0, angle[0])))
        angle[1] = math.acos(max(-1.0, min(1.0, angle[1])))
        angle[2] = math.acos(max(-1.0, min(1.0, angle[2])))
        for i in range(3):
            angle[i]= math.degrees(angle[i])
        return sorted(angle)