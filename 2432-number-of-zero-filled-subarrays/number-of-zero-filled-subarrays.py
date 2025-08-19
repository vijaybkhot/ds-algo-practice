class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0
        curr_map = defaultdict(int)

        for right in range(len(nums)):
            if len(curr_map) == 1 and 0 in curr_map and nums[right] != 0:
                curr_len = curr_map[0]
                count += (curr_len*(curr_len+1))//2
            curr_map[nums[right]] += 1
            while left < right and len(curr_map) > 1:
                curr_map[nums[left]] -= 1
                if curr_map[nums[left]] == 0:
                    del curr_map[nums[left]]
                left += 1
        
        if len(curr_map) == 1 and 0 in curr_map:
            curr_len = curr_map[0]
            count += (curr_len*(curr_len+1))//2
        
        return count
                
                