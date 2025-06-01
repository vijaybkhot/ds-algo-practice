class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        def dfs(curr_sum):
            if curr_sum == target:
                return 1
            if curr_sum > target:
                return 0
            if curr_sum in memo:
                return memo[curr_sum]
            total = 0
            for num in nums:
                total += dfs(curr_sum + num)
            memo[curr_sum] = total
            return total

        return dfs(0)
        