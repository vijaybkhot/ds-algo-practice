class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # prefix_sum = 0
        # for num in nums:
        #     prefix_sum += num
        
        # for i, j in queries:
        #     prefix_sum -= (j + 1 - i)
        #     if prefix_sum <= 0:
        #         return True
        
        # return prefix_sum <= 0
        # max_num, idx_max = nums[0], 0
        # for idx, num in enumerate(nums):
        #     if num > max_num:
        #         max_num = num
        #         idx_max = idx
        
        # for i, j in queries:
        #     if i <= idx_max <= j+1:
        #         max_num -= 1
        #     if max_num <= 0:
        #         return True
        
        
        # return max_num <= 0

        n = len(nums)
        delta = [0] * (n + 1)  # one extra to simplify range updates
        
        # Mark range updates
        for l, r in queries:
            delta[l] += 1
            if r + 1 < len(delta):
                delta[r + 1] -= 1
        
        # Apply prefix sum to get actual decrements at each index
        decrements = [0] * n
        curr = 0
        for i in range(n):
            curr += delta[i]
            decrements[i] = curr
        
        # Final check
        for i in range(n):
            if nums[i] - decrements[i] > 0:
                return False
        
        return True


        