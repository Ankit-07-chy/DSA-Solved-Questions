class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        player = 0
        score = [0]*2
        n = len(piles)
        start = 0; end = n-1

        while start <= end:
            if player == 0:
                # maximize
                if piles[start] >= piles[end]:
                    score[player] += piles[start]
                    start += 1
                else:
                    score[player] += piles[end]
                    end -= 1

            else:
                # minimize
                if piles[start] >= piles[end]:
                    score[player] += piles[end]
                    end -= 1
                else:
                    score[player] += piles[start]
                    start += 1

        return score[0] > score[1]
