class Solution:
    def integerBreak(self, n: int) -> int:
        # Bottom-up DP - O(n^2) solution
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1  # (max_product, index)

        for i in range(3, n+1):
            l, r = 1, i-1
            curr_max = float('-inf')
            while l <= r:
                curr_max = max(curr_max, max(dp[l], l) * max(dp[r], r))
                l += 1
                r -= 1
            dp[i] = curr_max
        return dp[n]

