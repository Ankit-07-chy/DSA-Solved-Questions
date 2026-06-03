class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = list(zip(landStartTime,landDuration))
        water = list(zip(waterStartTime,waterDuration))
        
        land.sort(key = lambda x: x[0]+x[1])
        water.sort(key=lambda x:x[0]+x[1])
        print(land,water)
        m1 = land[0][0] + land[0][1]
        temp = inf
        for k1,k2 in water:
            temp = min(temp,(max(m1,k1)+k2))
        

        m2 = water[0][0] + water[0][1]
        temp1 = inf
        for k1,k2 in land:
            temp1 = min(temp1,(max(m2,k1)+k2))
        return min(temp,temp1)

# Brute Force
'''
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
        return result'''