class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # left = 0
        # count = 0
        # curr_map = defaultdict(int)

        # for right in range(len(nums)):
        #     if len(curr_map) == 1 and 0 in curr_map:
        #         curr_len = curr_map[0]
        #         prev_len = curr_len - 1
        #         count -= (prev_len*(prev_len+1))//2
        #         count += (curr_len*(curr_len+1))//2
        #     curr_map[nums[right]] += 1
        #     while left < right and len(curr_map) > 1:
        #         curr_map[nums[left]] -= 1
        #         if curr_map[nums[left]] == 0:
        #             del curr_map[nums[left]]
        #         left += 1
        
        # if len(curr_map) == 1 and 0 in curr_map:
        #     curr_len = curr_map[0]
        #     count += (curr_len*(curr_len+1))//2
        
        # return count

        count = 0
        streak = 0

        for num in nums:
            if num == 0:
                streak += 1
                count += streak
            else:
                streak = 0
        
        return count
                
                