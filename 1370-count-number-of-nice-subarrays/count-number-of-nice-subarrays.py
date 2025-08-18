class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # # using mathematical formula: exact(k) = atmost(k)-atmost(k-1)
        # def atMostKOdds(nums, k):
        #     left = 0
        #     count = 0
        #     odd_count = 0
        #     for right in range(len(nums)):
        #         if nums[right]%2:
        #             odd_count += 1
                
        #         while (right - left + 1) >= k and odd_count > k:
        #             if nums[left]%2:
        #                 odd_count -= 1
        #             left += 1
        #         count += right - left + 1
            
        #     return count
        
        # return atMostKOdds(nums, k) - atMostKOdds(nums, k-1)

        # using three pointer sliding window
        l, m = 0, 0
        count = 0
        odd = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l
            if odd == k:
                while not nums[m]%2:
                    m += 1
                count += m-l+1
        
        return count