class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Solution using hash map - O(n) extra space
        # Create a hash-map of index:value as key value pairs
        index_map = {}
        for index, num in enumerate(nums):
            index_map[index] = num
        
        for index, num in index_map.items():
            new_index = (index + k) % len(nums)
            nums[new_index] = num