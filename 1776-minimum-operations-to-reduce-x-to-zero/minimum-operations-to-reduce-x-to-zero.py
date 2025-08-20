class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # nums.sort()
        
        # min_size = float('inf')
        # left = 0
        # curr_sum = 0

        # for right in range(len(nums)):
        #     curr_sum += nums[right]
        #     while curr_sum > x:
        #         curr_sum -= nums[left]
        #         left += 1
            
        #     if curr_sum == x:
        #         min_size = min(min_size, right - left + 1)
        
        # return min_size if 

        # l, r = 0, len(nums)-1
        # ops = 0

        # while l <= r:
        #     if x == 0:
        #         return ops
            
        #     if x < nums[l] and x < nums[r]:
        #         print(x, nums[l], nums[r])
        #         return -1
            
        #     if nums[r] > nums[l]:
        #         if x >= nums[r]:
        #             x -= nums[r]
        #             r -= 1
        #         elif x >= nums[l]:
        #             x -= nums[l]
        #             l += 1
        #         ops += 1
        #     else:
        #         if x >= nums[l]:
        #             x -= nums[l]
        #             l += 1
        #         else:
        #             x -= nums[r]
        #             r -= 1
        #         ops += 1

        # return ops if x == 0 else -1 

        # [1,   1,  4,  2,  3], x = 5
        # 1,    2,  6,  8,  11

        # @lru_cache(None)
        # def dfs(l, r, x):
        #     if x == 0:
        #         return 0
        #     if x < 0 or l > r:
        #         return float('inf')
            
        #     # choose left:
        #     min_ops = 1 + dfs(l+1, r, x-nums[l])
        #     # choose right
        #     min_ops = min(min_ops, 1 + dfs(l, r-1, x-nums[r]))

        #     return min_ops
        
        # min_ops = dfs(0, len(nums)-1, x) 

        # if min_ops == float('inf'):
        #     return -1
        
        # return min_ops

        target = sum(nums) - x
        if target < 0: 
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1