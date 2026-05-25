class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * n, [0] * n
        f[0] = 1
        # since we start dynamic programming from i=minJump, we need to precompute the prefix sums for the part [0, minJump)
        for i in range(minJump):
            pre[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)
            pre[i] = pre[i - 1] + f[i]

        return bool(f[n - 1])


# This codes is correct but gives TLE,
"""
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        zero_idx = []
        visited = {}
        for i in range(n):
            if s[i]=='0':
                zero_idx.append(i)
                visited[i] = 0
        # visited = [0]*len(zero_idx)
        if s[-1] != '0':
            return False
        visited[0] = 1; i = 0 # to track of visited
        for idx in zero_idx:
            if visited[idx] == 1:
                #return False
                
                min_j = idx + minJump; max_j = min(idx+maxJump,n-1)
                if min_j <= n-1 <= max_j:
                    return True
                for ele in range(min_j,max_j+1):
                    if ele in visited:
                        visited[ele] = 1
        return visited[n-1] == 1
            



        '''
        n = len(s)
        if s[n-1] != '0':
            return False
        # zero_idx = [0]
        # # find index of all element which are '0'
        # for idx,val in enumerate(s):
        #     zero_idx.append(idx)
        # zero_idx_len = len(zero_idx)
        # print(n)
        idx  = 0; i = 0
        while True:
            min_j = idx + minJump
            max_j = min(idx+maxJump,n-1)
            print(min_j,max_j)
            
            if min_j <= n-1 <= max_j:
                return True
            if min_j > n-1:
                return False

            curr = min_j
            latest = idx
            while curr <= max_j:
                if s[curr] == '0':
                    latest = max(latest,curr)
                curr += 1
            if latest > idx:
                idx = latest
            else:
                return False
            print(latest)
        return False
        '''
        """