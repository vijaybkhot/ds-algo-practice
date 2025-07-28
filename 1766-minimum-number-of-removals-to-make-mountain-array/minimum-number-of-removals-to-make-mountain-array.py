class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # LIS from the left
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)
        
        # LDS from the right
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)
        
        max_mountain = 0
        for i in range(1, n - 1):  # Peak can't be at the ends
            if left[i] > 1 and right[i] > 1:
                max_mountain = max(max_mountain, left[i] + right[i] - 1)
        
        return n - max_mountain