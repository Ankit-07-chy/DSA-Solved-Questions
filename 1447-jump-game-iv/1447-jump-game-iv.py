from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:

        mapp = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in  mapp:
                mapp[arr[i]].append(i)
            else:
                mapp[arr[i]] = [i]
        
        visited = [0]*n
        q = deque([])
        steps = 0
        q.append(0)
        visited[0] = 1

        while q:
            if visited[n-1] == 1:
                return steps
            steps += 1
            q_size = len(q)
            while (q_size>0):
                q_size -= 1
                temp = q.popleft()
                prev = temp-1
                front = temp + 1
            
                if prev >= 0 and visited[prev] == 0:
                    q.append(prev)
                    visited[prev] = 1
                if front < n and visited[front] == 0:
                    q.append(front)
                    visited[front] = 1
                if arr[temp] in mapp:
                    elements = mapp[arr[temp]]
                    mapp.pop(arr[temp])
                    for element in elements:
                        if visited[element] == 0:
                            q.append(element)
                            visited[element] = 1
            
        return steps
