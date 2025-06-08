class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        # # Top down-DP
        # dp = {}
        # def dfs(i, M, alice):
        #     if i >= len(piles):
        #         return 0
        #     if (i, M, alice) in dp:
        #         return dp[(i, M, alice)]
        #     if alice:
        #         total = 0
        #         for k in range(1, 2*M+1):
        #             total = max(total, (sum(piles[i:i+k]) + dfs(i+k, max(M, k), False)))
        #     else:
        #         total = float('inf')
        #         for k in range(1, 2*M+1):
        #             total = min(total, (dfs(i+k, max(M, k), True)))

        #     dp[(i, M, alice)] = total
        #     return total
        
        # return dfs(0, 1, True)

        n = len(piles)
        dp = [[0]*(n+1) for _ in range(n+1)]
        suffix_sum = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] += suffix_sum[i+1] + piles[i]
        
        for i in reversed(range(n)):
            for M in range(1, n+1):
                for X in range(1, 2*M+1):
                    if i + X <= n:
                        dp[i][M] = max(dp[i][M], suffix_sum[i] - dp[i + X][max(M, X)])

        return dp[0][1]


        # Bottom-up DP



            