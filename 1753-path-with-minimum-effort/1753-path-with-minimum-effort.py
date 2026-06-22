import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights); col = len(heights[0])
        min_heap = []
        heapq.heappush(min_heap,[0,0,0])
        distance =[[inf]*col for i in range(row)]
        distance[0][0] = 0

        while min_heap:
            temp = heapq.heappop(min_heap)
            curr_level = temp[0]; i = temp[1]; j = temp[2]
            if i == row-1 and j == col-1:
                return curr_level
                
            indexes = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
            for index in indexes:
                if 0<=index[0]<row and 0<=index[1]<col:
                    next_level = abs(heights[index[0]][index[1]] - heights[i][j])
                    if next_level < distance[index[0]][index[1]] :
                        distance[index[0]][index[1]] = next_level
                        
                        heapq.heappush(min_heap,[max(next_level,curr_level),index[0],index[1]])
        return distance[row-1][col-1]