class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxi = 0
        for g in gain:
            curr = alt + g
            maxi = max(maxi,curr)
            alt = curr
        return maxi
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for g in gain:
            curr = alt[-1] + g
            alt.append(curr)
        return max(alt)'''