class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # return True     # The answer is alway true

        dp = {}
        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            # total = 0
            # if alice:
            #     total = max(piles[i] + dfs(i+1, j, not alice), piles[j] + dfs(i, j-1, not alice))
            # else:
            #     total = max((dfs(i+1, j, not alice) - piles[i]), (dfs(i, j-1, not alice) - piles[j]))
            # dp[(i, j, alice)] = total
            # return total

            left = piles[i] - dfs(i+1, j)
            right = piles[j] - dfs(i, j-1)
            
            dp[(i, j)] = max(left, right)
            return dp[(i, j)]


        return dfs(0, len(piles)-1) > 0

