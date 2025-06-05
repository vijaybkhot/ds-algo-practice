class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # # 2-D Dynamic Programming
        # n = len(stones)
        # dp = [[0]*n for _ in range(n)]
        # for r in range(n):
        #     for c in range(n):
        #         if r == c:
        #             dp[r][c] = stones[c]

        
        # for r in range(n-2, -1, -1):
        #     for c in range(n-1, r, -1):
        #         dp[r][c] = abs(dp[r+1][c]-stones[r])
        
        # return min(dp[0])

        stoneSum = sum(stones)
        target = (stoneSum + 1) // 2
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        return dfs(0, 0)