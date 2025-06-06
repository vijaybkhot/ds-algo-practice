class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # # Bottom-Up (Tabulation) Approach: Use 0/1 Knapsack DP to find the closest subset sum to half of the total, then compute the minimal difference.
        total = sum(stones)
        target = total // 2
        dp = [False]*(target+1)
        dp[0] = True

        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = dp[i] or dp[i-stone]
        
        for j in range(target, -1, -1):
            if dp[j]:
                return abs(j - (total - j))
        return 0
       

        # # Top-Down DP: Recursively try all possible partitions of the stones into two groups and memoize the minimal difference.
        # stoneSum = sum(stones)
        # target = (stoneSum + 1) // 2
        # dp = {}

        # def dfs(i, total):
        #     if total >= target or i == len(stones):
        #         return abs(total - (stoneSum - total))
        #     if (i, total) in dp:
        #         return dp[(i, total)]

        #     dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
        #     return dp[(i, total)]

        # return dfs(0, 0)