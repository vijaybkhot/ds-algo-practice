class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #  l                 r
        # [1,   1,  2,  1,  1]


    
        def atMostKOdds(nums, k):
            left = 0
            count = 0
            odd_count = 0
            for right in range(len(nums)):
                if nums[right]%2:
                    odd_count += 1
                
                while (right - left + 1) >= k and odd_count > k:
                    if nums[left]%2:
                        odd_count -= 1
                    left += 1
                count += right - left + 1
            
            return count
        
        return atMostKOdds(nums, k) - atMostKOdds(nums, k-1)