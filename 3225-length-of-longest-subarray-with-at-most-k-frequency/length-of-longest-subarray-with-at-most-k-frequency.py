class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        curr_map = defaultdict(int)

        for right in range(len(nums)):
            curr_map[nums[right]] += 1

            while left <= right and curr_map[nums[right]] > k:
                curr_map[nums[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res