class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l = 0; r = 0; count = 0
        while l < len(players):
            e = players[l]
            if r < len(trainers):
                if e <= trainers[r]:
                    count += 1
                    r += 1
                    l += 1
                else:
                    r += 1
            else:
                break

            
        return count
