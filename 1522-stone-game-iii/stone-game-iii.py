class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # # Greedy approach- Not correct for all tests
        # alice, bob = 0, 0
        # alice_turn = True
        # i = 0
        # while i < len(stoneValue):
        #     new_i = i
        #     one_stone, two_stone, three_stone, total = 0, 0, 0, 0
        #     one_stone = stoneValue[i]
        #     if i+1 < len(stoneValue):
        #         two_stone = one_stone + stoneValue[i+1]
        #     if i+2 < len(stoneValue):
        #         three_stone = two_stone + stoneValue[i+2]
            
        #     if one_stone > two_stone and one_stone > three_stone:
        #         total = one_stone
        #         new_i = i+1
        #     elif two_stone> one_stone and two_stone > three_stone:
        #         total = two_stone
        #         new_i = i+2
        #     else:
        #         total = three_stone
        #         new_i = i+3
        #     if alice_turn:
        #         alice += total
        #     else:
        #         bob += total
        #     alice_turn = not alice_turn
        #     i = new_i


        # if alice > bob:
        #     return "Alice"
        # elif bob > alice:
        #     return "Bob"
        # else:
        #     return "Tie"


        # Top-down DP
        n = len(stoneValue)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]

            res, total = float("-inf"), 0
            for j in range(i, min(i+3, n)):
                total += stoneValue[j]
                res = max(res, total - dfs(j+1))
            dp[i] = res
            return res
            
        total = dfs(0)
        return "Alice" if total > 0 else ("Bob" if total < 0 else "Tie")
        