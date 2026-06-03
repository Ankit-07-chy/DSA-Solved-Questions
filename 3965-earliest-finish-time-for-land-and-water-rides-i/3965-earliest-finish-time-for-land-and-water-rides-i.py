
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime); m = len(waterStartTime)
        result = inf
        for i in range(0,n):
            curr = landStartTime[i] + landDuration[i]
            for j in range(0,m):
                land_water = max(curr,waterStartTime[j]) + waterDuration[j]
                result = min(result,land_water)
        for i in range(0,m):
            curr = waterStartTime[i] + waterDuration[i]
            for j in range(0,n):
                land_water = max(curr,landStartTime[j]) + landDuration[j]
                result = min(result,land_water)
        return result