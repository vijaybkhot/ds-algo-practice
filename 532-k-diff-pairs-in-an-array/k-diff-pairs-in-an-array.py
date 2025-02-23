class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # # Brute force solution using sorting
        # nums.sort()
        # left = 0
        # right = 1
        # diff_pair = 0
        # while left < len(nums) and right < len(nums):
        #     right = left + 1
        #     curr_left = nums[left]
        #     possible_right = curr_left + k
        #     for i in range(right, len(nums)):
        #         if nums[i] == possible_right:
        #             diff_pair += 1
        #             break
        #     left += 1
        #     while left < len(nums) and nums[left] == curr_left:
        #         left += 1
        
        # return diff_pair

        # Efficient solution using hash map
        # Create a hash map to count frequency of each number in the array
        
        diff_pair = 0
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        # Get all keys in the map
        unique_nums = hash_map.keys()
        if k == 0:
            for num in unique_nums:
                if num in hash_map and hash_map[num] > 1:
                    diff_pair += 1
            return diff_pair

        for num in unique_nums:
            if num + k in hash_map:
                diff_pair += 1
        
        return diff_pair
        
            


            
        