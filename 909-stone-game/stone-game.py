class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # return True     # The answer is alway true

        dp = {}
        def dfs(i, j, alice):
            if i > j:
                return 0
            if (i, j, alice) in dp:
                return dp[(i, j, alice)]
            total = 0
            if alice:
                total = max(piles[i] + dfs(i+1, j, not alice), piles[j] + dfs(i, j-1, not alice))
            else:
                total = max((dfs(i+1, j, not alice) - piles[i]), (dfs(i, j-1, not alice) - piles[j]))
            dp[(i, j, alice)] = total
            return total

        return dfs(0, len(piles)-1, True) > 0

