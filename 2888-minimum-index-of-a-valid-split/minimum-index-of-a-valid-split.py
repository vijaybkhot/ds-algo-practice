class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Function to find the most frequent number (dominator) and its frequency
        def maxFreqNum(nums: List[int]) -> List[int]:
            freq_map = {}  # Dictionary to store frequency of each number
            max_freq = 0  # Track the maximum frequency found
            most_freq = nums[0]  # Track the most frequent number
            
            # Count frequencies of all numbers in nums
            for num in nums:
                freq_map[num] = freq_map.get(num, 0) + 1
                if freq_map[num] > max_freq:
                    most_freq = num
                    max_freq = freq_map[num]
            
            return [most_freq, max_freq]  # Return the most frequent number and its count
        
        # If there's only one element, it's impossible to split into two non-empty subarrays
        if len(nums) == 1:
            return -1
        
        # Find the most frequent number and its total occurrences
        most_freq_num, max_freq = maxFreqNum(nums)

        n = len(nums)  # Length of the array
        left_num_count = 0  # Count of the most frequent number in the left subarray

        # Iterate through the array, considering every possible split
        for i in range(n - 1):  # Stop at n-1 to ensure right subarray is non-empty
            if nums[i] == most_freq_num:
                left_num_count += 1  # Update count of most frequent number in left part
            
            left_len = i + 1  # Length of the left subarray
            right_len = n - left_len  # Length of the right subarray
            right_num_count = max_freq - left_num_count  # Count of most frequent number in right subarray

            # Check if the most frequent number is dominant in both halves
            if left_num_count > left_len // 2 and right_num_count > right_len // 2:
                return i  # Return the first valid split index
        
        return -1  # No valid split found