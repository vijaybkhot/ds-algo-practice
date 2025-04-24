class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        # # Brute force, In efficient approach:
        # distinct = len(set(nums))
        # count = 0
        # right = 0

        # while right < len(nums):
        #     curr_sub = nums[:right+1]
        #     curr_len = len(set(curr_sub))
        #     if curr_len == distinct:
        #         left = 0
        #         hold = curr_len
        #         while left < right+1 and curr_len >= distinct:
        #             curr_sub = nums[left:right+1]
        #             hold = len(set(curr_sub))
        #             if hold == distinct:
        #                 count += 1
        #             left += 1
        #     right += 1
        
        # return count

        # Sliding window approach using a hash map:
        total_distinct = len(set(nums))
        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) == total_distinct:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count
                        
                    