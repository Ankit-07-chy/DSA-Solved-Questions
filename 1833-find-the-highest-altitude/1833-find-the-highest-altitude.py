class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for g in gain:
            curr = alt[-1] + g
            alt.append(curr)
        return max(alt)