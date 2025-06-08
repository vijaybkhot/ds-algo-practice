class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = max(nums[i] - dfs(i+1, j), nums[j] - dfs(i, j-1))
            return dp[(i, j)]
        
        return  dfs(0, len(nums)-1) >= 0
        