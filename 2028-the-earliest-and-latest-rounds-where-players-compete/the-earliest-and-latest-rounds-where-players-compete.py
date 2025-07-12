class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer
        
        @lru_cache(None)
        def dfs(players: tuple, round_num: int):
            # If firstPlayer and secondPlayer are facing off
            for i in range(len(players) // 2):
                if (players[i] == firstPlayer and players[-i-1] == secondPlayer) or \
                   (players[i] == secondPlayer and players[-i-1] == firstPlayer):
                    return (round_num, round_num)
            
            next_states = set()
            m = len(players)
            choices = []
            for i in range(m // 2):
                a = players[i]
                b = players[m - i - 1]

                # If it's firstPlayer vs secondPlayer, they must face off — handled separately above
                if (a, b) == (firstPlayer, secondPlayer) or (a, b) == (secondPlayer, firstPlayer):
                    choices.append([firstPlayer])  # arbitrarily let firstPlayer win
                elif firstPlayer in (a, b):
                    choices.append([firstPlayer])  # force firstPlayer to win
                elif secondPlayer in (a, b):
                    choices.append([secondPlayer])  # force secondPlayer to win
                else:
                    choices.append([a, b])  # both could win

            # Now simulate all combinations of winners for this round
            for outcome in product(*choices):
                next_round = list(outcome)
                if m % 2 == 1:
                    next_round.append(players[m // 2])  # odd player auto-advances
                next_round.sort()
                next_states.add(tuple(next_round))
            
            min_r, max_r = float('inf'), float('-inf')
            for state in next_states:
                e, l = dfs(state, round_num + 1)
                min_r = min(min_r, e)
                max_r = max(max_r, l)
            
            return (min_r, max_r)
        
        return list(dfs(tuple(range(1, n + 1)), 1))