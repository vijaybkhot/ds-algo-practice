class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # @lru_cache(None)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     max_rob = nums[i] + dfs(i+2)
        #     max_rob = max(max_rob, dfs(i+1))

        #     return max_rob
        
        # return dfs(0)

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        max_num_1 = (nums[0], nums[1])

        for i in range(2, n):
            curr_max_set = (max(max_num_1), (nums[i]+max_num_1[0]))
            max_num_1 = curr_max_set

        
        return max(max_num_1)
