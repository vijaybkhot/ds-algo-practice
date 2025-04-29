class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        left = 0
        max_elem = max(nums)
        count = 0

        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            while freq_map[max_elem] >= k:
                count += (len(nums) - right)
                freq_map[nums[left]] -= 1
                left += 1
        
        return count

        