class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            max_rob = nums[i] + dfs(i+2)
            max_rob = max(max_rob, dfs(i+1))

            return max_rob
        
        return dfs(0)
