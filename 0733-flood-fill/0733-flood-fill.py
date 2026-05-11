import copy
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image  # <-- ONLY CHANGE: Early return if no change is needed
        # grid = image.copy -- I got MLE from here I don't know why?
        initial_color = image[sr][sc]
        image[sr][sc] = color
        row = len(image); col = len(image[0])
        q = deque([])
        q.append([sr,sc])
        while q:
            temp = q.popleft()
            adj = [[temp[0]+1,temp[1]],[temp[0]-1,temp[1]],[temp[0],temp[1]+1],[temp[0],temp[1]-1]]
            for ad in adj:
                if 0<=ad[0]<row and 0<=ad[1]<col and image[ad[0]][ad[1]] == initial_color:
                    image[ad[0]][ad[1]] = color
                    q.append([ad[0],ad[1]])
        
        return image