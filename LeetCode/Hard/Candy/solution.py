class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_neighbour = [0]*n
        right_neighbour = [0]*n
        left_neighbour[0] = 1; right_neighbour[-1] = 1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left_neighbour[i] = left_neighbour[i-1]+1
            else:
                left_neighbour[i] = 1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right_neighbour[i] = right_neighbour[i+1]+1
            else:
                right_neighbour[i] = 1
        ans = 0
        for i in range(n):
            ans += max(right_neighbour[i],left_neighbour[i])
        return ans