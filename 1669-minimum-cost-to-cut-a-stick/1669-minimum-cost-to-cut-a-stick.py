from functools import cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def f(i, j):
            if i >= j:
                return 0

            mini = float('inf')

            for cut in cuts:
                if i < cut < j:
                    cost = (j - i) + f(i, cut) + f(cut, j)
                    mini = min(mini, cost)
                # No cut exists between i and j
            if mini == float('inf'):
                return 0

            return mini

        return f(0, n)

# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:
#         c = len(cuts)
#         cuts.append(0); cuts.append(n); cuts.sort()
#         @cache
#         def f(i,j):
#             if i > j:
#                 return 0
#             maxi = 10**9 
#             for k in range(i,j+1):
#                 cost = cuts[j+1] - cuts[i-1] + f(i,k-1) + f(k+1,j)
#                 maxi = min(maxi,cost)
#             return maxi
#         return f(1,c)


# # class Solution:
# #     def minCost(self, n: int, cuts: List[int]) -> int:
# #         cuts.sort()

# #         @cache
# #         def f(i,j):
# #             if i >= j:
# #                 return 0
# #             mini = 0
           
# #             for cut in cuts:
                
# #                 if i<cut<j:
# #                     cost = j-i + f(i,cut) + f(cut,j)
# #                     mini = min(mini,cost)
# #             return mini
# #         return f(0,n)
