class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def maxFreqNum(nums: List[int]) -> int:
            freq_map = {}
            max_freq = 0
            most_freq = nums[0]
            for num in nums:
                freq_map[num] = freq_map.get(num, 0) + 1
                if freq_map[num] > max_freq:
                    most_freq = num
                    max_freq = freq_map[num]
            
            return [most_freq, max_freq]
        
        if len(nums) == 1:
            return -1
        
        [most_freq_num, max_freq] = maxFreqNum(nums)
        
        i = 0
        n = len(nums)
        left_num_count = 0
        while i < n-1:
            if nums[i] == most_freq_num:
                left_num_count += 1
            left_len = i+1
            right_len = n - left_len
            right_num_count = max_freq - left_num_count
            if left_num_count > left_len//2 and right_num_count > right_len//2:
                return i
            i += 1
        
        return -1






            
        