class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # max_sum = 0
        # # Initiate a window of len k
        
        # window = [nums[i] for i in range(k)]

        # curr_sum = sum(window)
        # if len(window) == len(set(window)):
        #     max_sum = curr_sum
        
        # left = 0
        # for right in range(k, len(nums)):
        #     # Remove left
        #     curr_sum -= window[0]
        #     window.pop(0)
        #     # Add right
        #     curr_sum += nums[right]
        #     window.append(nums[right])
        #     if len(window) == len(set(window)):
        #         max_sum = max(curr_sum, max_sum)
            
        #     left += 1
        # return max_sum

        # max_sum = 0
        # # Create a freq_map
        # freq_map = {}
        # # Initialize first window
        # for i in range(k):
        #     freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        # if max(freq_map.values()) == 1:
        #     max_sum = sum(freq_map.keys())
        # left = 0
        # for right in range(k, len(nums)):
        #     # Remove left
        #     freq_map[nums[left]] = freq_map.get(nums[left]) - 1
        #     if freq_map[nums[left]] == 0:
        #         del freq_map[nums[left]]
            
        #     # Add right element to window
        #     freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
        #     if max(freq_map.values()) == 1:
        #         max_sum = max(sum(freq_map.keys()), max_sum)
            
        #     left += 1

        
        # return max_sum

        # Using a duplicate counter
        max_sum = 0

        freq_map = {}
        duplicate_counter = 0
        # Initialize first window
        curr_sum = 0
        for i in range(k):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            curr_sum += nums[i]
            if freq_map[nums[i]] == 2:
                duplicate_counter += 1
        
        if duplicate_counter == 0:
            max_sum = curr_sum
        
        left = 0
        for right in range(k, len(nums)):
            # Remove left
            left_num = nums[left]
            freq_map[nums[left]] = freq_map.get(nums[left]) - 1
            curr_sum -= left_num
            if freq_map[nums[left]] == 1:
                duplicate_counter -= 1
            if freq_map[nums[left]] == 0:
                del freq_map[nums[left]]
            
            # Add right
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
            curr_sum += nums[right]
            if freq_map[nums[right]] == 2:
                duplicate_counter += 1
            
            if duplicate_counter == 0:
                max_sum = max(max_sum, curr_sum)
            
            left += 1


        return max_sum


        
        