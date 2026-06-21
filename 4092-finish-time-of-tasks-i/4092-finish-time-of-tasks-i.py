class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:

        tree = [[] for i in range(n)]
        for u,v in edges:
            tree[u].append(v)

        def dfs(node):
            if not tree[node]:
                return baseTime[node]
            child_times = [dfs(child) for child in tree[node]]
            earliest = min(child_times)
            latest = max(child_times)
            own = (latest-earliest)+baseTime[node]
            return latest + own 
        return dfs(0)