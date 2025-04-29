class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # # First attempt: Using a dictionary to track the frequency of each number in sub-array and tracking the frequency of max element
        # freq_map = defaultdict(int)
        # left = 0
        # max_elem = max(nums)
        # count = 0

        # for right in range(len(nums)):
        #     freq_map[nums[right]] += 1
        #     while freq_map[max_elem] >= k:
        #         count += (len(nums) - right)
        #         freq_map[nums[left]] -= 1
        #         left += 1
        
        # return count

        # More optimized approach - No dictionary. Just keep track of frequency of max element in a counter

        left = 0
        max_elem = max(nums)
        count = 0
        freq = 0

        for right in range(len(nums)):
            if nums[right] == max_elem:
                freq += 1
            while freq >= k:
                count += (len(nums) - right)
                if nums[left] == max_elem:
                    freq -= 1
                left += 1
        
        return count



        