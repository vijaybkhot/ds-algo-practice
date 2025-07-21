class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1  # Set bottom-right + one-step cells to 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                min_health_needed = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = max(1, min_health_needed)

        return dp[0][0]