class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        count = 0
        curr_sum = 0
        #       l
        # [1,   0,  1,  0,  1]
        #                   r
        # sum = 2
        # count = 2
        # for r in range(len(nums)):
        #     curr_sum += nums[r]
        #     if curr_sum == goal:
        #         count += 1
        #     start = l
        #     end = l
        #     while l <= r and curr_sum > goal:
        #         curr_sum -= nums[l]
        #         l += 1
            
            
            
        # return count

        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        prefix = 0
        count = 0

        for idx, num in enumerate(nums):
            prefix += num
            if prefix-goal in prefix_map:
                count += prefix_map[prefix-goal]
            prefix_map[prefix] += 1
        
        return count