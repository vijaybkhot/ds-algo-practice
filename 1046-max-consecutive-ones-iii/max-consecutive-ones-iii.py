class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        left = 0
        max_len = 0

        for right in range(len(nums)):
            counter[nums[right]] += 1

            while left <= right and counter[0] > k:
                counter[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len

        