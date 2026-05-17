

"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def find_index(arr):
            val = 0
            for i in range(len(arr)):
                if arr[i] == val:
                    return i 

        index_0 = find_index(arr)
        n = len(arr)
        memo = [-1]*(n+1)
        def reach(idx,index_0,arr):
            if arr[idx] == 0:
                return True
            if idx == index_0:
                # memo[idx] = 1
                return True 
            if memo[idx] != -1:
                return memo[idx]

            front = idx + arr[idx]
            find_front = False
            if front < n:
                find_front = reach(front,index_0,arr)
                # memo[front] = find_front
                
            back = idx - arr[idx]
            find_back = False
            if 0<=back:
                find_back = reach(back,index_0,arr)
                # memo[back] = find_back 
            
            # ans = find_front or find_back 
            memo[idx] = find_front or find_back 
            return memo[idx]
        return reach(start,index_0,arr)
        
"""
from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True

        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            for jump in [idx + arr[idx], idx - arr[idx]]:
                if 0 <= jump < n and not visited[jump]:
                    visited[jump] = True
                    queue.append(jump)
        return False