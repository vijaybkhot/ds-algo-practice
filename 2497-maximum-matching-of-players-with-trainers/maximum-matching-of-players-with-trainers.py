class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i, j = 0, 0
        match = 0
        while i < len(players) and j < len(trainers):
            while j < len(trainers) and players[i] > trainers[j]:
                j += 1
            if i < len(players) and j < len(trainers) and players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
        
        return match
