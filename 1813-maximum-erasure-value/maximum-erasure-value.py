class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_sum = 0
        left = 0
        curr_map = defaultdict(int)
        res = 0

        for right in range(len(nums)):
            curr_map[nums[right]] += 1
            curr_sum += nums[right]
            while left <= right and curr_map[nums[right]] > 1:
                curr_map[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1
            
            res = max(res, curr_sum)
        
        return res

            