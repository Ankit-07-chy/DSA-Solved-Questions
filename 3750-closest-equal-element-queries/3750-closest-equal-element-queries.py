class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums_pos = defaultdict(list)

        for i in range(n):
            nums_pos[nums[i]].append(i)

        for pos in nums_pos.values():
            x = pos[0]
            pos.insert(0, pos[-1] - n)
            pos.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = nums_pos[x]
            if len(pos_list) == 3:
                queries[i] = -1
                continue
            pos = bisect.bisect_left(pos_list, queries[i])
            queries[i] = min(
                pos_list[pos + 1] - pos_list[pos],
                pos_list[pos] - pos_list[pos - 1],
            )

        return queries

'''from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for q_idx in queries:
            query_val = nums[q_idx]
            curr = float('inf')
            
            for j in range(n):
                if query_val == nums[j] and q_idx != j:
                    straight_dist = abs(j - q_idx)
                    circular_dist = n - straight_dist
                    curr = min(curr, straight_dist, circular_dist)
            
            if curr != float('inf'):
                result.append(curr)
            else:
                result.append(-1)
        
        return result

# class Solution:
#     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         len_queries = len(queries)
#         n = len(nums)
#         result = []
#         for i in range(len_queries):
#             # query index
#             q_idx = queries[i]
#             query = nums[q_idx]
#             curr = float('inf')
#             for j in range(n):
#                 if query == nums[j] and i != j:
#                     straight_dist = abs(j-q_idx)
#                     circular_dist = n - straight_dist
#                     curr = min(curr,straight_dist,circular_dist)
#             if curr != float('inf'):
#                 result.append(curr)
#             else:
#                 result.append(-1)
#         return result

'''