class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(1, len(nums)+1):
        #     count_increased = False
        #     l = 0
        #     r = 0
        #     window_prod = 1
        #     for _ in range(i):
        #         window_prod *= nums[r]
        #         r += 1
        #     while r <= len(nums):
        #         if window_prod < k:
        #             print(l, r)
        #             count += 1
        #             count_increased = True
        #         window_prod /= nums[l]
        #         l += 1
        #         window_prod *= nums[r] if r < len(nums) else 1
        #         r += 1
        #     if not count_increased:
        #         break
        
        # return count

        count = 0
        l = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            count += (r-l+1)
        
        return count

            
            
