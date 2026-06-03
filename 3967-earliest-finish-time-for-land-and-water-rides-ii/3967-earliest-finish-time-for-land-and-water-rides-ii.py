class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = list(zip(landStartTime,landDuration))
        water = list(zip(waterStartTime,waterDuration))


        land.sort(key=lambda x:x[0]+x[1])
        water.sort(key=lambda x:x[0]+x[1])
        temp1 = inf; temp2 = inf
        m1 = land[0][0] + land[0][1]
        for k1,k2 in water:
            temp1 = min(temp1,(max(m1,k1)+k2))
        n1 = water[0][0] + water[0][1]
        for k1,k2 in land:
            temp2 = min(temp2,(max(n1,k1)+k2))
        return min(temp1,temp2)
